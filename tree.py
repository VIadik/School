import turtle
turtle.left(90)
def tree(l, level):
    if level != 0:
        turtle.forward(((l ** 2) / 2) ** 0.5)
        turtle.right(45)
        tree(((l ** 2) / 2) ** 0.5, level - 1)
        turtle.left(90)
        tree(((l ** 2) / 2) ** 0.5, level - 1)
        turtle.right(45)
        turtle.backward(((l ** 2) / 2) ** 0.5)
    else:
        turtle.forward(l)
        turtle.backward(l)
        return
tree(110, 7)
turtle.mainloop()