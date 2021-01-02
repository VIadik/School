
import turtle

def Cross(l, level):
    if level != 0:
        Cross(l / 3, level - 1)
        turtle.left(90)
        Cross(l / 3, level - 1)
        turtle.right(90)
        Cross(l / 3, level - 1)
        turtle.right(90)
        Cross(l / 3, level - 1)
        turtle.left(90)
        Cross(l / 3, level - 1)
    else:
        turtle.forward(l)
        return

Cross(400, 4)

turtle.mainloop()