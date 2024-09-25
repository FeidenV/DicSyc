
define e = Character("Eileen")
define gui.text_font = "Roboto-Regular.ttf"
define gui.text_axis = {"width" : 125}
image mapbg = "map.jpg"

style blackcock:
    color "#000"

# The game starts here.

label start:
    show text "я КАРТА я карта Я Карта" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve

    camera:
        perspective True

    scene mapbg:
        zoom 1.58
        xpos 960 ypos 540 zpos-400
        anchor(0.5, 0.5)

    camera:
        perspective True
        zpos 0
        ease 1.0 xpos -100 zpos -600 
    show text "{color=#000}КЛИК{/color}" at truecenter 
    pause
    camera:
        perspective True
        xpos -100 zpos -600
        ease 1.0 xpos 0 ypos 0 zpos 0 matrixtransform RotateMatrix(0,0,0)
        ease 1.0 xpos 200 ypos 100 zpos -600 matrixtransform RotateMatrix(20,0,0)
    pause
    camera:
        perspective True
        xpos 200 ypos 100 zpos -600
        ease 1.0 xpos 0 ypos 0 zpos 0 matrixtransform RotateMatrix(0,0,0)
        ease 1.0 xpos 200 ypos -100 zpos -600 matrixtransform RotateMatrix(20,0,0)
    pause
    pause
    return
