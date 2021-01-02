import turtle
turtle.left(90)
def Branch(l, level):
    if level != 0:
        turtle.forward(l / 2 * 0.8)
        turtle.right(45)
        Branch(l / 4, level - 1)
        turtle.left(90)
        Branch(l / 4, level - 1)
        turtle.right(45)
        Branch(l / 2, level - 1)
        turtle.forward(l  / 2 * 0.8)
        turtle.backward(l * 0.8)
    else:
        turtle.forward(l)
        turtle.backward(l)
        return

Branch(300, 3)
turtle.mainloop()