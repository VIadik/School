
import turtle

def minkowski(l, level):
    if level != 0:
        minkowski(l / 3, level - 1)
        turtle.left(90)
        minkowski(l / 3, level - 1)
        turtle.right(90)
        minkowski(l / 3, level - 1)
        turtle.right(90)
        minkowski(l / 3, level - 1)
        minkowski(l / 3, level - 1)
        turtle.left(90)
        minkowski(l / 3, level - 1)
        turtle.left(90)
        minkowski(l / 3, level - 1)
        turtle.right(90)
        minkowski(l / 3, level - 1)
    else:
        turtle.forward(l)
        return

minkowski(799, 3)

turtle.mainloop()