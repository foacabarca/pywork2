# ！python3
# coding=utf8
"""
Project: 见缝插针
Author: 宋加运
Date: 2022/3/2 22:09
"""

from turtle import *
import random
import time

n = 0  # 全局变量n，方便计算针的数量，方便写循环
needles = []  # 存储所有针


class Needles:
    """ 包含针的长度和角度 """
    def __init__(self, length, angle):
        self.length = 200
        self.angle = 180


def draw_a_circle(c):
    """
    draw_a_circle: 画一个特定大小和颜色的填充圆，将针插在上面
    param c: 圆的填充颜色
    """
    penup()
    goto(0, -100)
    setheading(0)
    fillcolor(c)
    begin_fill()
    circle(100)
    end_fill()
    penup()


def draw_a_needle():
    """ 画出固定于面板左侧的针发射位置 """
    penup()
    goto(-360, 0)
    pensize(5)
    pencolor('purple')
    pendown()
    goto(-295, 0)
    pensize(5)
    pencolor('orange')
    goto(-270, 0)
    penup()


def spin_needles():
    """ 让针旋转起来：使用for循环更新每一个针的角度，长度不用改变 """
    global needles
    global n
    i = 0
    for i in range(n):
        needles[i].angle = needles[i].angle+1


def draw_needles():
    """ 根据插上去之后的每一根针的角度从而将其画出 """
    global needles
    global n
    i = 0
    for i in range(n):
        penup()
        goto(0, 0)  # 坐标（0，0）也是圆盘的圆心
        setheading(needles[i].angle)  # 调整海龟的方向，从而画出更新后的针
        pensize(3)
        pencolor("green")  # 先画绿色是为了和圆盘的颜色相同，从而显示出针是插在了圆盘表面
        pendown()
        forward(100)  # 此处的100也是圆盘的半径长度
        pencolor("orange")
        forward(100)
        penup()


def new_needle():
    """
    随机发射出一根针，此处需使用到random库，
    产生的随机数 a 为 0 到 100 内的整数，
    若 a < 5，则产生新的一根针，并加入到 needles 中
    """
    global n
    global needles
    a = random.randint(0, 100)
    # 如果a < 5，则创建新针并添加到needles中，n也相应加1
    if a < 5:
        newneedle = Needles(200, 180)
        needles.append(newneedle)  # 增加新针
        n = n + 1


def stop():
    """
    判断新插入的针是否和已有的针插在一起（这里指角度相差小于3度），
    若插在一起则圆盘变红，程序停止，等待鼠标点击结束
    """
    global n
    global needles
    for i in range(n):
        if abs(n-1-i) > 0 and abs(needles[n-1].angle - needles[i].angle) < 3:  # 如果新插入的针和已有的针角度相差小于3度
            draw_a_circle('red')  # 圆盘变成红色
            time.sleep(1.5)  # 暂停1.5s
            exitonclick()  # 等待点击结束


def main():
    hideturtle()  # 隐藏海龟的图标
    speed(0)  # 绘画速度最快
    # 每次循环针的角度加1，默认循环50*360次，即50圈
    for r in range(0, 18000):
        tracer(False)  # 隐藏绘图，直接显示绘画结果
        clear()  # 清屏，接着将更新后的针画出来
        draw_a_circle('green')
        draw_a_needle()
        new_needle()
        spin_needles()
        draw_needles()
        time.sleep(0.01)
        tracer(True)
        stop()
    done()


if __name__ == "__main__":
    main()
