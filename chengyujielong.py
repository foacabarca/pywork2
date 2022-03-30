from pypinyin import lazy_pinyin as lp
from turtle import *


def find_idiom():
    file = open("chengyu_utf8.txt", encoding="utf-8", mode="r")
    idioms_ = open("idioms.txt", 'w').close()
    idioms = open("idioms.txt", encoding="utf-8", mode="a")
    idioms.write("见缝插针\n")
    pin_yin = ['zhen']
    for f in file.readlines():
        if lp(f[0]) == pin_yin and f[3] != " ":
            idioms.write(f[0:4])
            idioms.write("\n")
            pin_yin = lp(f[3])
    file.close()
    idioms.close()


def write_idiom():
    i = 200
    penup()
    with open("idioms.txt", encoding="utf-8", mode="r") as idioms:
        for idiom in idioms.readlines():
            goto(200, i)
            pendown()
            write(idiom[0:4], font=("Consolas", 12, "normal"))
            penup()
            i = i - 20


find_idiom()
write_idiom()
exitonclick()
