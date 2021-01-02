
import turtle



def koch(l, level):
    if level != 0:
        koch(l / 3, level - 1)
        turtle.left(60)
        koch(l / 3, level - 1)
        turtle.right(120)
        koch(l / 3, level - 1)
        turtle.left(60)
        koch(l / 3, level - 1)
    else:
        turtle.forward(l)
        return

koch(600, 6)

turtle.mainloop()