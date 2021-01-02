import turtle
turtle.up()
turtle.goto(-200, 0)
turtle.down()
def Ice_Tri(l, level):
    if level != 0:
        Ice_Tri(l / 2, level  - 1)
        turtle.left(120)
        Ice_Tri(l / 3 * 0.8, level - 1)
        turtle.left(180)
        Ice_Tri(l / 3 * 0.8, level - 1)
        turtle.left(120)
        Ice_Tri(l /  3 * 0.8, level - 1)
        turtle.right(180)
        Ice_Tri(l / 3 * 0.8, level - 1)
        turtle.left(120)
        Ice_Tri(l / 2, level - 1) 
    else:
        turtle.forward(l)
turtle.tracer(0)
Ice_Tri(400, 4) 
turtle.update()
turtle.mainloop()