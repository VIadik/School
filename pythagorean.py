import turtle
def Pythagorean(l, level):
    if level != 0:
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.left(180)
        turtle.forward(l)
        turtle.right(45)
        Pythagorean(((l  ** 2) / 2)**0.5, level - 1)
        turtle.right(45)
        turtle.forward(l)
        turtle.left(135)
        turtle.forward(((l ** 2) / 2) ** 0.5)
        turtle.left(180)
        Pythagorean(((l  ** 2) / 2)**0.5, level - 1)
        turtle.forward(((l ** 2) / 2) ** 0.5)
        turtle.right(45)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        turtle.left(180)
        
    else:
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.left(90)

Pythagorean(80, 3)
turtle.mainloop()