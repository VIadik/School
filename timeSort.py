# Vlad Burmistrov April 2020
import random
import sys
import time
import turtle
from turtle import *


def qsort(a):
    if len(a) > 1:
        m = len(a) // 2
        b = []
        c = []
        d = []
        for i in range(len(a)):
            if a[i] == a[m]:
                d.append(a[i])
            elif a[i] < a[m]:
                c.append(a[i])
            else:
                b.append(a[i])
        return qsort(c) + d + qsort(b)
    else:
        return a


def merge(a, b):
    pa = pb = 0
    c = []
    while pa < len(a) and pb < len(b):
        if a[pa] < b[pb]:
            c.append(a[pa])
            pa += 1
        else:
            c.append(b[pb])
            pb += 1
    c += a[pa:]
    c += b[pb:]
    return c


def merge_sort(A):
    left = A[:len(A) // 2]
    right = A[len(A) // 2:]
    if len(A) > 1:
        left = merge_sort(left)
        right = merge_sort(right)
    return merge(left, right)


def array(n):
    A = []
    for i in range(n):
        A.append(random.randint(0, 10 ** 16))
    return A


num = []
for i in range(10000, 410000, 10000):
    num.append(i)
print(num)
time1 = []
time2 = []
time3 = []
n = []
for i in range(len(num)):
    A = array(num[i])
    B = A[::]
    C = A[::]
    D = A[::]
    start = time.process_time()
    merge_sort(B)
    t1 = round(time.process_time() - start, 6)
    start = time.process_time()
    qsort(C)
    t2 = round(time.process_time() - start, 6)
    start = time.process_time()
    sorted(D)
    t3 = round(time.process_time() - start, 6)
    print(num[i], t1, t2, t3)
    n.append(num[i])
    time1.append(t1)
    time2.append(t2)
    time3.append(t3)
x, y = -600, -320
mx, my = 333, 64
up()
goto(-600, -320)
down()
for i in range(4):
    forward(300)
    right(90)
    forward(5)
    up()
    forward(15)
    turtle.write(str((1 + i) * 100000), False, align="center", font=("Arial", 14, "normal"))
    backward(25)
    down()
    forward(5)
    left(90)
forward(20)
right(135)
forward(10)
backward(10)
right(90)
forward(10)
turtle.write("кол-во эл.", False, align="right", font=("Arial", 14, "normal"))
up()
goto(x - 10, y)
turtle.write("0", False, align="center", font=("Arial", 14, "normal"))
goto(x, y)
down()
right(45)
for i in range(5):
    forward(128)
    right(90)
    forward(5)
    backward(10)
    up()
    backward(10)
    turtle.write(str((1 + i) * 2), False, align="center", font=("Arial", 14, "normal"))
    forward(15)
    if (1 + i) * 2 == 10:
        up()
        forward(5)
        turtle.write("время, с.", False, align="left", font=("Arial", 14, "normal"))
        backward(5)
        down()
    left(90)
    down()
forward(20)
right(135)
forward(10)
backward(10)
right(90)
forward(10)
up()
goto(x, y)
down()
pencolor("red")
for i in range(len(n)):
    goto(x + n[i] / mx, y + time1[i] * my)
up()
goto(x, y)
down()
pencolor("green")
for i in range(len(n)):
    goto(x + n[i] / mx, y + time2[i] * my)
up()
goto(x, y)
down()
pencolor("blue")
for i in range(len(n)):
    goto(x + n[i] / mx, y + time3[i] * my)
up()
goto(-550, 300)
right(135 + 90)
down()
forward(40)
up()
forward(25)
pencolor("black")
goto(-500, 290)
turtle.write("Встроенная сортировка.", True, align="left", font=("Arial", 16, "normal"))
pencolor("green")
goto(-550, 275)
down()
forward(40)
up()
forward(25)
pencolor("black")
goto(-500, 265)
turtle.write("Быстрая сортировка.", True, align="left", font=("Arial", 16, "normal"))
pencolor("red")
goto(-550, 250)
down()
forward(40)
up()
forward(25)
pencolor("black")
goto(-500, 240)
turtle.write("Сортировка слиянием.", True, align="left", font=("Arial", 16, "normal"))
forward(2000)
mainloop()
# Vlad Burmistrov  April 2020
