

# Objects definition
=====================================
header                  id  header
menu                    css #menu
content                 id  content
side-panel              id  side-panel
footer                  id  footer

menu-item-*             css #menu li a

=====================================


@ Skeleton | all
-------------------------------
header
    inside: screen 0px top, 0px left, 0px right

menu
    inside: screen 0px left right
    below: header 0px

content
    below: menu 0px
    inside:screen 0px left

@ ^ | desktop
--------------
side-panel
    below: menu 0px
    inside: screen 0px right
    width: 300px
    near: content 0px right

@ ^ | mobile
--------------
content, side-panel
    width: 100% of screen/width


side-panel
    below: content 0px


@ Menu | desktop
-----------------------
[ 1 - 4 ]
menu-item-@
    height: 50 px

menu-item-*
    width: ~ 60 px

[ 1 - 3]
menu-item-@
    near: menu-item-@{+1} 0 to 10 px left

@ ^ | mobile
-----------------------------
[ 1, 2]
menu-item-@
    above: menu-item-@{+2} 0 to 10 px

[ 1, 3 ]
menu-item-@
    near: menu-item-@{+1} 0 to 10px left

