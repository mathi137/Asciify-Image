import requests
import validators

import numpy as np
import cv2
import os

import argparse
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def hex_to_ansi(hex_color: str) -> str:
    """Convert a hex color (#RRGGBB) to an ANSI escape code for the terminal."""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f'\033[38;2;{r};{g};{b}m'


class Asciify:
    # Default set of characters
    chars = (' ', '.', ';', 'c', 'o', 'P', 'O', '?', '@', '█')

    def __init__(self, chars: tuple[str] | list[str] = None) -> None:
        if chars:
            self.chars = chars

    def resize_image(self, image: np.ndarray, target_width=240, char_aspect_ratio=2, scale_x: float=None, scale_y: float=None) -> np.ndarray:
        height = image.shape[0] / char_aspect_ratio
        width = image.shape[1]

        aspect_ratio = height / width
        target_height = int(target_width * aspect_ratio)

        if scale_x and scale_y:
            resized_image = cv2.resize(image, dsize=(0, 0), fx=scale_x, fy=scale_y / char_aspect_ratio, interpolation=cv2.INTER_AREA)
        else:
            resized_image = cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)

        return resized_image

    def quantize_image(self, image: np.ndarray) -> np.ndarray:
        """Quantize an image to a limited set of characters."""
        num_chars = len(self.chars)
        bins = np.linspace(0, 255, num_chars + 1)

        # Use np.digitize to find the index of the closest bin for each pixel value
        indices = np.digitize(image, bins) - 1

        # Clip the indices to be within the valid range
        indices = np.clip(indices, 0, num_chars - 1)

        # Use np.vectorize to apply the chars mapping to the indices
        return np.vectorize(lambda x: self.chars[x])(indices)

    def invert_image(self, image) -> np.array:
        return 255 - image

    def sobel_filter(self, image) -> tuple[np.array, np.array]:
        gx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        gy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

        return gx, gy

    def compute_edges(self, gx: np.ndarray, gy: np.ndarray, threshold: float = 1.0) -> np.ndarray:
        """Compute edge map from Sobel gradients."""
        magnitude = np.sqrt(gx ** 2 + gy ** 2)
        mean_magnitude = np.mean(magnitude[magnitude >= np.mean(magnitude)])
        edge_threshold = threshold * mean_magnitude

        # edge_threshold = threshold * np.max(magnitude)
        # edge_threshold = np.mean(magnitude[magnitude >= np.mean(magnitude)])

        angles = np.arctan2(gx, gy) / np.pi * 0.5 + 0.5
        quantized_angles = np.round(angles * 8) / 8

        edge_map = np.full(magnitude.shape, ' ', dtype='U1')
        edge_mask = magnitude > edge_threshold

        slash_mask      = (quantized_angles == 0.125) | (quantized_angles == 0.625)
        backslash_mask  = (quantized_angles == 0.375) | (quantized_angles == 0.875)
        vertical_mask   = (quantized_angles == 0.25)  | (quantized_angles == 0.75)
        horizontal_mask = (quantized_angles == 0.5)   | (quantized_angles == 0)     | (quantized_angles == 1)

        edge_map[edge_mask & slash_mask]        = '/'
        edge_map[edge_mask & backslash_mask]    = '\\'
        edge_map[edge_mask & vertical_mask]     = '|'
        edge_map[edge_mask & horizontal_mask]   = '_'

        return edge_map

    def compute_dog(self, image, sigma=1.6, k=1.6, p=20.0, threshold=1.0) -> tuple[np.array, np.array]:
        """Compute Difference of Gaussians and apply thresholding."""
        # Convert to LAB color space and extract luminance (L channel)
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l_channel = lab[:, :, 0].astype(np.float32) * (100.0/255.0)  # Scale to 0-100 range

        # Apply Gaussian blurs (horizontal and vertical combined)
        blur1 = cv2.GaussianBlur(l_channel, (0, 0), sigmaX=sigma)
        blur2 = cv2.GaussianBlur(l_channel, (0, 0), sigmaX=sigma*k)

        # Calculate Difference of Gaussians
        dog = (1 + p) * blur1 - p * blur2
        dog = np.maximum(dog, 0)  # Remove negative values

        # Apply thresholding (simple version of shader's threshold logic)
        threshold_value = threshold
        dog_thresholded = np.where(dog >= threshold_value, 0, 255).astype(np.uint8)

        # Normalize for visualization
        dog_normalized = cv2.normalize(dog, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

        return dog_normalized, dog_thresholded
    
    def asciify(
            self, image_path: str, target_width=148, scale_x=None, scale_y=None, invert_colors=False, char_aspect_ratio=2.0, 
            dog_sigma=1.6, dog_k=1.6, dog_p=20.0, dog_threshold=1.0, edge_threshold=0.8
        ) -> np.array:
        
        if validators.url(image_path): 
            # Load image from URL
            response = requests.get(image_path)
            image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
            if image is None: raise ValueError('Image not found or unable to load.')

        else:
            # Load image file and check for errors
            image = cv2.imread(image_path)
            if image is None: raise ValueError('Image not found or unable to load.')
        
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized_image = self.resize_image(gray_image, target_width=target_width, char_aspect_ratio=char_aspect_ratio, scale_x=scale_x, scale_y=scale_y)
        
        # Invert image colors
        if invert_colors: resized_image = self.invert_image(resized_image)
        
        # Quantize the resized image to ASCII characters
        ascii_quantized = self.quantize_image(resized_image)
        
        # Compute the Difference of Gaussians and threshold it
        dog_normalized, dog_thresholded = self.compute_dog(image, sigma=dog_sigma, k=dog_k, p=dog_p, threshold=dog_threshold)
        dog_resized = self.resize_image(dog_thresholded, target_width=target_width, char_aspect_ratio=char_aspect_ratio)
        gradient_x, gradient_y = self.sobel_filter(dog_resized)
        
        # Compute edge map from gradients
        edge_map = self.compute_edges(gradient_x, gradient_y, threshold=edge_threshold)
        
        # Combine edge map and quantized ASCII characters
        ascii_art = np.where(edge_map != ' ', edge_map, ascii_quantized)

        return ascii_art
    
    def ascii_to_image(self, ascii_art: str, file_path: str, dpi: int, font_size=8, bg_color='black', color='white') -> None:
        """Convert ASCII art to an image and save it to a file."""
        plt.text(0, 0, ascii_art, fontfamily='monospace', fontsize=font_size, color=color)
        plt.axis('off')
        plt.savefig(file_path, dpi=dpi, facecolor=bg_color, bbox_inches='tight', pad_inches=0)


    def crop_rectangle(self, ascii_art: np.array, width: int, height: int, x_offset: int, y_offset: int) -> np.array:
        """Crop the image on a rectangle."""
        # Use full dimensions if width or height are not provided.
        if not width:
            width = ascii_art.shape[1]
        if not height:
            height = ascii_art.shape[0]

        # Determine the center of the crop in ascii-art (matrix) coordinates.
        center_row = ascii_art.shape[0] // 2 + y_offset
        center_col = ascii_art.shape[1] // 2 + x_offset

        # Calculate the start and end indices for rows and columns.
        start_row = center_row - height // 2
        end_row   = center_row + (height - height // 2)     # Ensures proper handling for odd heights.
        start_col = center_col - width // 2
        end_col   = center_col + (width - width // 2)       # Similarly for columns.

        # Clip the indices to the image boundaries.
        start_row = max(0, start_row)
        end_row   = min(ascii_art.shape[0], end_row)
        start_col = max(0, start_col)
        end_col   = min(ascii_art.shape[1], end_col)

        # Ensure the bounding box is valid.
        if start_row >= end_row or start_col >= end_col:
            print(f'{bcolors.FAIL}Bounding box out of range.{bcolors.ENDC}', end='\n\n')
            exit()

        cropped_art = ascii_art[start_row:end_row, start_col:end_col]
        return cropped_art


    def crop_circle(self, ascii_art: np.array, radius: int, char_ratio: float, x_offset: int, y_offset: int) -> np.array:
        """Crop the image on a circle."""
        # Default radius: half the true height.
        if not radius:
            radius = (ascii_art.shape[0] * char_ratio) / 2

        # Compute the center in true coordinates.
        center_true_y = (ascii_art.shape[0] * char_ratio) / 2 + y_offset * char_ratio
        center_true_x = ascii_art.shape[1] / 2 + x_offset

        # Determine the bounding box (in true coordinates) that encloses the circle.
        start_true_y = center_true_y - radius
        end_true_y   = center_true_y + radius
        start_true_x = center_true_x - radius
        end_true_x   = center_true_x + radius

        # Convert true coordinates to ascii-art indices.
        # For rows, we convert by dividing by char_ratio.
        start_row = int(max(0, np.floor(start_true_y / char_ratio)))
        end_row   = int(min(ascii_art.shape[0], np.ceil(end_true_y / char_ratio)))
        # For columns, true_x is the same as the column index.
        start_col = int(max(0, np.floor(start_true_x)))
        end_col   = int(min(ascii_art.shape[1], np.ceil(end_true_x)))

        # Ensure the bounding box is valid.
        if start_row >= end_row or start_col >= end_col:
            print(f'{bcolors.FAIL}Bounding box out of range.{bcolors.ENDC}', end='\n\n')
            exit()

        # Crop the ascii_art to the bounding box.
        cropped_art = ascii_art[start_row:end_row, start_col:end_col].copy()

        # Create a grid of indices corresponding to the cropped region.
        i_indices, j_indices = np.meshgrid(
            np.arange(start_row, end_row),
            np.arange(start_col, end_col),
            indexing='ij'
        )

        # Convert these indices to true coordinates.
        true_y = i_indices * char_ratio  # vertical coordinate in true units
        true_x = j_indices               # horizontal coordinate remains the same

        # Compute the Euclidean distance (in true units) from each cell to the circle's center.
        distances = np.sqrt((true_y - center_true_y) ** 2 + (true_x - center_true_x) ** 2)

        # Set cells outside the circle to a space.
        cropped_art[distances > radius] = ' '

        return cropped_art


def get_args() -> argparse.Namespace:
    class ShowColorsAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            print(f'Available colors: {list(mcolors.CSS4_COLORS.keys())}', end='\n\n')
            parser.exit()

    parser = argparse.ArgumentParser(description='Asciify an image.')

    # General arguments
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.1.0')
    parser.add_argument('--colors', '-clrs', action=ShowColorsAction, nargs=0, help='List available colors')

    # Arguments for asciifying an image
    parser.add_argument('--image', '-i', type=str, required=True, help='Path or URL to the image')
    parser.add_argument('--chars', '-chrs', type=str, nargs='+', default=None, help='Characters to be used for asciifying the image')
    parser.add_argument('--width', '-w', type=int, default=192, help='Width of the output ascii art')
    parser.add_argument('--fx', '-fx', type=float, default=None, help='Horizontal scaling factor')
    parser.add_argument('--fy', '-fy', type=float, default=None, help='Vertical scaling factor')
    parser.add_argument('--char-ratio', '-chr', type=float, default=2.0, help='Character aspect ratio')
    parser.add_argument('--sigma', '-sig', type=float, default=1.6, help='Sigma value for edge detection')
    parser.add_argument('--k', '-k', type=float, default=1.6, help='K value for edge detection')
    parser.add_argument('--p', '-p', type=float, default=20.0, help='P value for edge detection')
    parser.add_argument('--dog_threshold', '-dog-t', type=float, default=1.0, help='Threshold value for edge detection')
    parser.add_argument('--edge_threshold', '-edge-t', type=float, default=0.8, help='Threshold value for edge detection')
    parser.add_argument('--invert', '-inv', action='store_true', help='Invert colors')

    # Arguments to crop the image on a rectangle
    parser.add_argument('--crop-rectangle', '-cr', action='store_true', help='Crop the image on a rectangle')
    parser.add_argument('--crop-height', '-ch', type=int, default=None, help='Height of the rectangle')
    parser.add_argument('--crop-width', '-cw', type=int, default=None, help='Width of the rectangle')

    # Arguments to crop the image on a circle
    parser.add_argument('--crop-circle', '-cc', action='store_true', help='Crop the image on a circle')
    parser.add_argument('--crop-radius', '-rad', type=int, default=None, help='Radius of the circle')

    # Arguments to offset the cropped image
    parser.add_argument('--offset-x', '-ox', type=int, default=0, help='Offset X coordinate')
    parser.add_argument('--offset-y', '-oy', type=int, default=0, help='Offset Y coordinate')
    
    # Arguments for outputing the ascii art to an image
    # parser.add_argument('--output', '-o', type=str, default=None, help='Path to the output file')
    parser.add_argument('--output', '-o', action='store_true', help='Path to the output file')
    parser.add_argument('--dpi', '-d', type=int, default=100, help='DPI of the output image')
    parser.add_argument('--font-size', '-fs', type=int, default=8, help='Font size of the output image')
    parser.add_argument('--background', '-bg', type=str, default='black', help='Background color of the output image')
    parser.add_argument('--color', '-c', type=str, default='white', help='Text color of the output image')

    return parser.parse_args()


def main() -> None:
    args = get_args()

    if args.color.lower() not in mcolors.CSS4_COLORS.keys():
        print(f'{bcolors.FAIL}Invalid color. Please enter a valid color name.\nAvailable colors: {list(mcolors.CSS4_COLORS.keys())}{bcolors.ENDC}', end='\n\n')
        exit()

    color_hex = mcolors.CSS4_COLORS[args.color.lower()]
    color_code = hex_to_ansi(color_hex)

    asciify = Asciify(args.chars)
    ascii_art = asciify.asciify(
        args.image, target_width=args.width, char_aspect_ratio=args.char_ratio,  scale_x=args.fx, scale_y=args.fy, invert_colors=args.invert,
        dog_sigma=args.sigma, dog_k=args.k, dog_p=args.p, dog_threshold=args.dog_threshold, edge_threshold=args.edge_threshold
    )

    if args.crop_rectangle:
        ascii_art = asciify.crop_rectangle(ascii_art, args.crop_width, args.crop_height, args.offset_x, args.offset_y)
    elif args.crop_circle:
        ascii_art = asciify.crop_circle(ascii_art, args.crop_radius, args.char_ratio, args.offset_x, args.offset_y)

    ascii_str = '\n'.join(''.join(row) for row in ascii_art)

    ascii_path = './ascii'
    if not os.path.exists(ascii_path):
        os.makedirs(ascii_path)

    with open(os.path.join(ascii_path, 'ascii.txt'), 'w+', encoding='UTF-16') as f:
        f.write(ascii_str)

    if args.output:
        # Saving the ascii art as image
        print(f'{bcolors.OKCYAN}Generating image...{bcolors.ENDC}', end='\n\n')
        if not os.path.exists('./images'):
            os.makedirs('./images')

        file_path = os.path.join('./images', os.path.basename(args.image).split('.')[0] + '.png')

        asciify.ascii_to_image(
            ascii_str, file_path=file_path, dpi=args.dpi, font_size=args.font_size, bg_color=args.background, color=args.color
        )
    else:
        print(f'{bcolors.WARNING}Output not activated. To save the ascii art, use the --output (-o) option.{bcolors.ENDC}', end='\n\n')

    print(f'{color_code}{ascii_str}{bcolors.ENDC}', end='\n\n')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'{bcolors.FAIL}An error occurred: {e}{bcolors.ENDC}', end='\n\n')