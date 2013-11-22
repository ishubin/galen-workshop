

# Objects definition
=====================================
header                  id  header
menu                    css #menu
content                 id  content
side-panel              id  side-panel
footer                  id  footer
=====================================


@ all
-------------------------------
header
    inside: screen 0px top, 0px left, 0px right

menu
    inside: screen 0px left right
    below: header 0px

content
    below: menu 0px
    inside:screen 0px left

@ desktop
--------------------------------
side-panel
    below: menu 0px
    inside: screen 0px right
    width: 300px
    near: content 0px right

@ mobile
--------------------------------
content, side-panel
    width: 100% of screen/width


side-panel
    below: content 0px




