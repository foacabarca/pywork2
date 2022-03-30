from pypinyin import lazy_pinyin as lp
from turtle import *


def write_idioms():
    file = open("chengyu_utf8.txt", encoding="utf-8", mode="r")
    penup()
    goto(200, 220)
    pendown()
    write("见缝插针", font=("Consolas", 13, "normal"))
    penup()
    i = 192
    count = 0
    pin_yin = ['zhen']
    end_word = "针"
    for f in file.readlines():
        if lp(f[0]) == pin_yin and f[3] != " " and count < 10:
            goto(200, i)
            pendown()
            write(f[0:4], font=("Consolas", 13, "normal"))
            count = count + 1
            penup()
            i = i - 28
            pin_yin = lp(f[3])
            end_word = f[3]
    if count == 9:
        goto(200, i-20)
        pendown()
        write("接龙结束", font=("Consolas", 13, "normal"))
        penup()
    file.close()

