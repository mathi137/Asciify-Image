# Asciify Image

![](./examples/example.gif)

-------------------------------------------------------------------------------------------------------

## What Asciify Image is

Asciify is a Python script that generates ASCII art by using the luminance of each pixel and mapping it to a specified character equivalent.
It also computes the gradient of the image to draw contours using vertical lines, underlines, backslashes, and slashes.

-------------------------------------------------------------------------------------------------------
## Example

![example1](./examples/example1.jpeg)
Credits: [xai](https://x.com/xyanaid)
![ascii_example1](./images/example1.png)
```
;;|;...|               ||;;;;;;;..           |.;;;;;. |..;cooooocooooooooooooooooo|;|;|.|;||||..| ..||.|c;|c|| ||oPoPPPPPPPPPPPPPPPPPPPPPPPPPPPPooc|cc;;cc;;cc;;;;;;ccocc;.| |  ...;;;|| |   .| 
;c/_  _/      _/_|   /_/;\_____   ___       //;/_//_._//__ooooocooooooooooooooooo/|;/;;;;;||/.|/  . /|./c//o|| ||PPoPPPPPPPPPPPPPPPPPPPPPPPooooc/_;|....;;;;;;;;;__..\\ccc_\.\__....\\;\.\\   \
_/|_/_      /___ |   |;;....   /_      /  _/;;_/_  //_/oooPPooooooooooooooooooooo|;;;/;|;;|.|.|| ../.|.c;/oo//|||PooPPPPPPPPPPPPPPPPPPPPo______;/..\___/_ccc__oo______/;ccc\\\ . ....\\\\ \.  .
;./_  /    _/  |/   ..  __  ___     /_  /_;;/_..___/_ooPPPoooooooPPooooooooooooo//;;;;/c;;|.|.|| . /|.c;//o|//||oPoPPPPPPPPPPPPPPPPPo___/;....|.\//;;;ccooPPPPPPPPPoo_ccc\oc\\_/. ....\;\\\ . \
___     __// __/  __/___         __  ___c;/.. /___ooPPPPPoooooPPPooooooooooooooo|;;.;/c;;/..../ . |..;c;/oP|| ||PPoPPPPPPPPPPPPPPocc;;;;...___/cc_ccocooPPPPPPPPPPPPPPoo\coooc__.......\;\  .|
      /__       _____         ___   __;/__  __/coooPPP_oooPPoPPPooooPoooooooooo/|;;./cc;;;...// . |..c;//oP||//|PPoPPPPPPPPPP___/___.....;;ccoooooPPPPPPPPPPPPPPPPPPPPPoPoooPooc;..._\..\;\ _.
__           ____      _   __/  ___.\_/| //...;c_______\_oooooPooPPoooooooooooo|;;.//c;;;;.../ . /..;c;/oP||.//PPPoPPPPPPPP//_;........;c/_oPPPPPPPPPPoPoPPPOOPPPPPPPPPPPPoooooooc.....\.|.\|\
                       _____  _/__.. ..__/...;....;.....______\coooooooooooooo|/;.//oc;;;..|/  . |.;c;/ooP||||oPPPPPPPPP___/;....___/___PPPPPPPPPPPPPPoPoPPPPPPPPPPPPPPPoPPooooPoo\\.....\_.\ \
            _       __ /__ ____;;;;____/_cc__cc_______;_\.....\\;cccc_oooooooo//../ooc;;;..||   ||.;;//ooP||||PPPPPPPPoc;;......//__oPPPPPPPPPPPPPPPPPoPoPPPPPPPPPPPPPPPPPPoooPPPoc\\.._./\\\\
                 __ /__ ___/;;;;cc;/oooooo_PPPPPoooooooo\_____;;;;;;;;__\cooo//..//oc;;;...| /| |.;c;/ooP|| //PPPPPooc_;;;;;__///oPPPPPPPPPPPPPPPPPPPPoooPPPPPPPPPPPPPPPPoPPooPPPPocc;\.\. \\\\
     _         _   _  ___/;;;ccccc/PPPPooPPPPPPoPPPPPPPococoo\__ccccc_;;|coo//..;/ooc;;;..|/  | ..c;/oooP||||PPPPooocc;cc;;/___PPPPPPPPPPPPoooooooooooooooPPPPPoPPoPPPPPPooPooooPPoocc\\ \. \.|
  _             _ __//__ccccoooo_/PPPPooPPPPPPPPPPPPPPo_coooPPPPPoocoo\c;co//./;/occ;c;.|.| || ..c;//PoPP||//PPPPPPPocc____PoPPPPooPPPPooocoooooPP___PPoP______PPPPooooooooPPoooooooocc\|\\. \ _
            /_   /__/ccooooPPPPPPPPPoooPPPPPPPPPPPPP__/c|ooPPPPPPPoPPPPocco/;/;;oocc;;|.||| \/ .;;c/oPoP/|||oPPPPPPPPPoPPPPPPPooooooooocoooPPo________________________ooooooPooPoooooocc\\\\\ \
     __\ /_/  /__/ccoooPPPPPPPPOPPPPooPPooooooooccccccccooooPoPPPPPPPPPPPo/;/;;cooccc;;..||\  ..c//oPoPP||||PPPPPPPPPPPPPPPPPoooooooooooooo____/_  ...\ .______..._________ooooooooooooo\\\\.\ _
     | \__ ./__cccooPPPPPPPPPPPPPoooc_/ooP_PPooooooo_coocccccoPoPPPPPPPPP/c/;cc/ooccc|...||   |c;/ooooP//.|/PPPPPPPPPPPPPPPPooooooooooo_____.  __/  //\_..|___________|._\\\ccooooooooooo\\ |.\
  _\ / ..___/oocoPPOOPPPPPPPPPPPPo/cc__ccc___________oPPPPoocccoPPPPPPPP/c/cccoocccc;|.||/   |;;|/oPoPP||||PPPPPPPPPPPPPPPPoooooocooo/__..  /_/__....\..|/\\PPPPPP____\___.;\cccoooooooooo\\\\|
./_\  /___/PP/_|oPPPPPPP_______/__....__;......_/.\______\oPoooccooPPPP/c/oocooocccc;|.||||  |cc/oPoPPo|\//PPPPPPPPPPPPPPPooooocoooo//./__\.;.\\/.;/.|..\\.\\POOOPPPPPo_____/cccooooooooooc| \
_/ /__/ooPPPP/c/Pooooo_____...;;;;_/___oo;...  ___\ /   \\__\ooooocooPoc/ooooPocccc;;...| | //;/coPoPP||//oPPPPPPPPPPPPPPooooooooo/_;..|..|\_.......//...\\||POOOOOOOPoc;cccccooooooooooooo|||
 /__/ooooPoo|c|ooo/;;//.___________oooP|/\.. _\ ../__.___  /\\_\ooo/cco_oooooP/cccc;;..||   |;//oPoPPo/;//PPPPPPPPPPPPPPPooooooo/_;/c|/\\...__\ ..___....||||OOOOOOOOoc/;cccccooooooooooooo|| |
.||PPPoooooo|c|occ;;;\_//c__PPPOPPPPOPP|/|... \\//\|;....__\ \____/c/oooooooP|c|coc;|.|||  /cc/ooPoPP//c|PPPPPPPPPPPPPPPPoooooo/;c//P|\._\.....\........./|//OOOOOOOPoc;c_/oooooooooooooooo|| \
;||PPPPPPPPP|c|ooo_oc__ocoooPOOPOOOOOOO|.|..;\ ././;;......|\//;.__o/oooooooP|cooo;;...|||//;/ooPoPPocc/oPPPPPPPPPPPPPPPPPPPoo/;//PPP\\\.\\............._/;/OOOOOOOPooooooooooooooooooooooo||||
;|oPPPPPPPPP|o|PPPoooocccc_oPOOOOOOOOOO|||...\__\.... |....|||/\__;\\oooooooocococc;..// //_/ooPPPPPoo/ooPPPPPPPPPPPPPPPPPPPocc_/POOOPP\\_._______/___;;;_/OOOOOOOPPoocoooooPPPPPPPoooooooPo|||
;|PoPPPPPPPO|o|PPPPPooooo|;|oOOOOOOOOOO\\|../  .    .. ...;/.//PP__cc\oooooPocoooc;;;.//|/;coooPPP/ooPPoPPPPPPPPPPPPPPPPPPPooPPPOOOOOOOO\\__.....;;;;;c___OOOOOOOPooooooPPPPPPPPPPPPPPPooPPo|||
_\PPPoPPPPOOPPOOPPPPPPoooo_coPOOOOOOOOOO\_..../ .........._.//POOPP\\cooooPPoooPooc;;///||coooPPP/oo/PPPPPPPPPPPPPPPPPPPPPPPPPPOOOOO__OOOOO____________???OOOPPooPooooPPPPPPPPPPPPPPPPPoPPoo|||
_\\PPPPPPOOOPOOOOPPPPPPPPoo|c\POOOOOOOOOO\\;._...__...__;.;//OOOOOOPP_ooPoPPooPoPoo;;|| ||oooPPP/oo/PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPooooooPPOOOOOOOOOOOOOOOOPPPoooooPPPPPPPPPPPPPPPPPPPPooPPo||\/
 \\\PPPPPOOOOOOOOOOPPPPPPPoo\cooPOOOOOOOOOP\\;;_...;;;;;c__/OOOOOOOOOPPooPPoooPPPoo;//||||oPoPPP/o/PPPPPPPPPPPPPPPPPPPPPPPPPPPooooooo_oooPPP_________________ooooPPPPPPP___________________/|.
_|\\PPOOOOOOOOOOOOOOOPPPPPPPPoooo___________OOPPPoPPPOO?OOO________OOOPPoPooooPP|cc;// /||PPPPPPo/PPPPOOOOOOOOOOOOPPPPPPPPPPPPPo_oo_______________________/________________________________;;...
_| \\OOOOO__________________________________o__oooo________________\o_____oooPPP|cc/| ///oPPPPPoPPPPPPOOOOOOOOOOOOOOOPPPPPP___________ccccc;__\___cccc__cccccc_//cccccc\_____________________;;;
 | |\_______________;;;;;;;;;;;;__________________________________ccc;;;;;c___ooo;;|| ///PPPPPPPPPPPPOOOOOOOOOOOOOOOOOOP____;;;ccc_______________________________________________________oooccoc
_|||;_/__;c________________________________OO______________________oo\____\;__\\;;;||||cPPPPOPPPOOPPPOOOOOOOOOOOOOOOOP//_;;/__________PPPPPPPPPPPPPOOOOOOOOOOPPPPOOOOOOOOOOOOOOOOOOOOoc;;;;;;;/_
 ||/;;;/_c//________OOOOOOOOOOOOOOOOOOOPPPOOPPOOOPPOOOOPPPPPPPPPPPPPPPPPoo\__\.\\;// //oP___PPP______________OOO___P//_;____OOOOOOOOOOOPPPPPPPPPPPPPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoc;;;;;__;;
  |c/\/PPc/oPOOOOPPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPPPPPPOOOOOOPPPPPPP____;_/ //co/_________________________ccc|/__/OOOOOOOOOOOOOOOOOOOPPPPPPPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPocccc;;;;;c
__c/.//occcoPPOOOPPPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPPOPPPoPPPPPPPP|//|/;;/;;;_;;;______________cccc__c\_/OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPocccc;;;;cc
__|||/ccccccPPOOOOPPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPPPPOOPPPPPPPPPP/| |\\;;/_________________________??\oPO___/_\OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOPccccc;;;ccc
cc||||cccccccPOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO?@@@@█@@@?__\/|.//;;c__?@@@██@@███████████████████@OPPooooc\\??@???@@???OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOocccc;;cccoo
_\\\||occccccoO??OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO??@@███████████//_\/|/...//??██████?█████████████████████@/o/_\\\c|██████████@@@@@???????OOOOOOOOO??????@@@@@@@?OOOOOOOPccoP|ccccooO
_\c|||occcccccP?@@@@??OOOOOOOOOOOOOOOOOOOO????OOOOOO???@@@████████████████//Poo/.|/.|/O?██████@@██████████████████████|_\OO?P_/@████████████████████@@@@@@@@@@██████████████@?OOOOOocoPPoccooPPo
  \;.||oooooooo_@███████@@@????OOO??????????@@@@@@@███████████████████████|o__|||.///P?@█████@@███████████████████████\|\\OOO@████████████████████████████████████████████████@?OOPccccccooPOP/c
_\ |;\\PPPPPPooc\@███████████████████████████████████████████████████████|OOPO/..|//P?@██████@█████████████████████████\o\??@██████████████████████████████████████████████████@?PoccccoooPOP//_
 | |.;\\PPPPPPP\oO████████████████████████████████████████████████████████\??//|..//?@██████@██████████████████████████\\o\████████████████████████████████████████████████████@OocccoooPOOP//;P
 | | .;\\oPPPPPP\oO@████████████████████████████████████████████████████████\|.|.;/??██████@@███████████████████████████\\\\███████████████████████████████████████████████████?PcoooPPOOOoo/|/?
_\    ..\\\PPOPPPPoO@██████████████████████████████████████████████████████@/|...//@██████@@█████████████████████████████\_O\████████████████████████████████████████████████@?PoooPPPO_/___|P@?
.\\     .\\\PPOPPPPoO@████████████████████████████████████████████████████@///..//@███████@███████████████████████████████\\P\\█████████████████████████████████████████████@?PooPPOOP/ooPO?P█O█
_.\\    \.__\\POOPPPPP@███████████████████████████████████████████████████//_..//@███████@█████████████████████████████████@\P\\███████████████████████████████████████████@?PPPOOOOPPoO??@P█O/█
 \_       |.\\\\OOPPooP?@████████████████████████████████████████████████@/|..//@███████@███████████████████████████████████\\OP\@████████████████████████████████████████@?OOOOOO//oO@??@P█O/██
__        \ |._\\OOOPPoo__\█████████████████████████████████████████████_/|\.//|██████████████████████████████████████████████\_OOO__█████████████████████████████████████@?OOO/_\oo\__@@P█O\\__
 _\_        / /\|PPPO_OOPo\_█████████████████████████████████████████__Ooc..///@█████████████████████████████████████████████████@OOO?__@████████████████████████████████@____Poco/cc;cc;;;/oooP
_\ \\         |\|@@?OPPOOOOP?@████████████████████████████████████___PoPPc;;//?████████████████████████████████████████████████████__OPP_______@████████████████@@█______OOoooP_o/_|_oc_P_______
 \_           \ \\███__OPO?@@@@██████████████████████████████____?PoP__Oo|;//?████████████████████████████████████████████████████████__?PoPPOO?_________________@?OOPoooP____OO//.|ocoOo/OOOOOO
  ___  __  \   \.\\██████@?OOO?@_____███████████████████_____OPoPP___??P//;/@███████████████████████████████████████████████████████████_______OPPPPPPPPPPPPPPPoPPP______??@@@@//||\;oPo/PPPOOOO
          \ |  | \\\█████████@@??OPOO?____████████___@??OPPPP____?@@@?O//;//████████████████████████████████████████████████████████████████████_________________@@@@@@@@@@@@@///. \\cco|PPPPOOO
            | |\\ \\\████████████____??OOO??O??????OO???_____@███@@@?O?|c//█████████████████████████████████████████████████████████████████████████████████@@@@@@@@@@@@@@@@@///    __|oo\PPPPOO
.|  |         |  | |||█████████████████████████████████████████@@@@?OOo|P|███████████████████████████████████████████████████████████████████████████████████@@█@@@@@@@@@@@@O||      ||PPoPPPPPO
```

-------------------------------------------------------------------------------------------------------
## How to use

- Install all the dependencies from ```requirements.txt```
- Run python ```asciify.py -i examples/example1.jpeg```
- To view all available arguments and features, run ```python asciify.py --help```
- Have fun!

-------------------------------------------------------------------------------------------------------
## Credits

Heavily inspired on [Acerola's Ascii Shader](https://github.com/GarrettGunnell/AcerolaFX/blob/main/Shaders/AcerolaFX_ASCII.fx) 

-------------------------------------------------------------------------------------------------------
## References

- [Acerola FX](https://github.com/GarrettGunnell/AcerolaFX/blob/main/Shaders/AcerolaFX_ASCII.fx)
- [XDoG Paper](https://users.cs.northwestern.edu/~sco590/winnemoeller-cag2012.pdf)

