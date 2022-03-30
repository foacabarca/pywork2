from pypinyin import lazy_pinyin as lp
from turtle import *


def find_idiom(file, pin_yin):
    with open(file, "r") as file:
        with open("idioms.txt", "a") as idioms:
            for f in file.readline():
                if lp(f[0]) == pin_yin:
                    idioms.write(f[0:4])
                    idioms.write("\n")
                    pin_yin = lp(f[3])


def write_idiom(t):
    i = 200
    penup()
    with open("idioms.txt", "r") as idioms:
        for ff in idioms.readline():
            goto(200, i)
            pendown()
            write(i, font=("JatBrains Mono", 12, "normal"))
            penup()
            i = i - 20
