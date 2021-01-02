
import turtle

def Levy(l, level):
    if level != 0:
        turtle.left(45)
        Levy(((l ** 2)/2)**0.5, level - 1)
        turtle.right(90)
        Levy(((l ** 2)/2)**0.5, level - 1)
        turtle.left(45)
    else:
        turtle.forward(l)
        return

Levy(400, 10)
turtle.mainloop()