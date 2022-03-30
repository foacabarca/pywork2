from pypinyin import lazy_pinyin as lp
from turtle import *


def find_idiom(all_idioms_txt, idioms_txt, pin_yin):
    with open(all_idioms_txt, encoding="utf-8", mode="r") as file:
        with open(idioms_txt, encoding="utf-8", mode="a") as idioms:
            for f in file.readline():
                if lp(f[0]) == pin_yin:
                    idioms.write(f[0:4])
                    idioms.write("\n")
                    pin_yin = lp(f[3])


def write_idiom(idioms_txt):
    i = 200
    penup()
    with open(idioms_txt, encoding="utf-8", mode="r") as idioms:
        for idiom in idioms.readline():
            goto(200, i)
            pendown()
            write(idiom, font=("Consolas", 12, "normal"))
            penup()
            i = i - 20
