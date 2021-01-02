import turtle
def Ice_Rect(l, level):
    if level != 0:
        Ice_Rect(l / 2, level - 1)
        turtle.left(90)
        Ice_Rect(l / 2 * 0.75, level - 1)
        turtle.right(180)
        Ice_Rect(l / 2 * 0.75, level - 1)
        turtle.left(90)
        Ice_Rect(l / 2, level - 1)
        
    else:
        turtle.forward(l)
        return
turtle.tracer(0)
Ice_Rect(400, 1)
turtle.update()
turtle.mainloop()
