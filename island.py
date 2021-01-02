import turtle
def Island(l, level):
    if level != 0:
        turtle.left(45)
        Island(((l ** 2) / 2) ** 0.5 / 2, level - 1)
        turtle.right(90)
        Island(((l ** 2) / 2) ** 0.5 / 2, level - 1)
        Island(((l ** 2) / 2) ** 0.5 / 2, level - 1)
        turtle.left(90) 
        Island(((l ** 2) / 2) ** 0.5 / 2, level - 1)
        turtle.right(45)
    
    
    else:
        turtle.forward(l)
        return
Island(300, 3)

turtle.mainloop()