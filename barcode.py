from turtle import *


def draw_barcode(bar_code):
    h = 110
    w = 3
    x = 50
    y = -290
    speed(0)
    penup()
    for i in bar_code:
        fillcolor("black" if i == "1" else "white")
        begin_fill()
        goto(x, y)
        goto(x + w, y)
        goto(x + w, y + h)
        goto(x, y + h)
        goto(x, y)
        end_fill()
        x += w
    goto(0, 0)


def write_information():
    penup()
    goto(80, -160)
    pencolor("black")
    pendown()
    write("计203  宋加运  42024130", font=("Consolas", 12, "normal"))
    penup()

