from turtle import *


def draw_barcode(bar_code):
    """
    将turtle移至合适位置
    画出每一条的边框填充形成条形码
    :param bar_code:二进制形式的条形码字符串
    :return: None
    """
    h = 110  # 条形码高度110
    w = 3  # 条形码每一条宽3
    x = 50
    y = -290
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
    """
    调整turtle至合适位置写下个人信息
    :return: None
    """
    penup()
    goto(75, -170)
    pendown()
    write("计203  宋加运  42024130", font=("Consolas", 16, "bold"))
    penup()
