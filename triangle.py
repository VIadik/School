import turtle
def Triangle(l, level):
    if level != 0:
        Triangle(l / 2, level - 1)
        turtle.forward(l / 2)
        Triangle(l / 2, level - 1)
        turtle.left(60)
        turtle.forward(l / 2)
        turtle.left(120)
        turtle.forward(l / 2)
        turtle.left(180)
        Triangle(l / 2, level - 1)
        turtle.right(120)
        turtle.forward(l / 2)
        turtle.left(120)
    else:
        turtle.forward(l)
        turtle.left(120)
        turtle.forward(l)
        turtle.left(120)
        turtle.forward(l)
        turtle.left(120)
Triangle(400, 7)
turtle.mainloop()