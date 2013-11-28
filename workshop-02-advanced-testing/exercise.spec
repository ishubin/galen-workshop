===============

box-*           css     .box
box-*-icon      css     .box .icon

===============

@ Boxes | all 
----------------------------------
[ 1 - 5 ]
box-@-icon
    centered all inside: box-@  5px

[ 1 - 5]
box-@
    height: ~ 200px



@ ^ | desktop
--------------
[ 1 - 4 ]
box-@
    near: box-@{+1} 20px left


@ ^ | tablet 
----------------
[ 1 - 5 ]
box-@
    width: 43 to 50% of screen/width

[ 1 - 2 ]
box-@
    above: box-@{+2} 20px

box-5
    below: box-3 20px


@ ^ | mobile
--------------
[ 1 - 5 ]
box-@
    width: 90 to 100% of screen/width

[ 1 - 4 ]
box-@
    above: box-@{+1} 20px
