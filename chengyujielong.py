from pypinyin import lazy_pinyin as lp
from turtle import *


def write_idioms():
    file = open("chengyu_utf8.txt", encoding="utf-8", mode="r")
    penup()
    goto(200, 250)
    pendown()
    write("见缝插针", font=("Consolas", 13, "normal"))
    penup()
    i = 222
    count = 0
    pin_yin = ['zhen']
    end_word = "针"
    for f in file.readlines():
        if lp(f[0]) == pin_yin and f[3] != " " and count < 10 and f[0] != end_word:
            goto(200, i)
            pendown()
            write(f[0:4], font=("Consolas", 13, "normal"))
            count = count + 1
            penup()
            i = i - 28
            pin_yin = lp(f[3])
            end_word = f[3]
    file.close()
    # 第一次遍历后成语不够，再次从头遍历，遍历条件相同
    if count < 10:
        file2 = open("chengyu_utf8.txt", encoding="utf-8", mode="r")
        for f2 in file2.readlines():
            if lp(f2[0]) == pin_yin and f2[3] != " " and count < 10 and f2[0] != end_word:
                goto(200, i)
                pendown()
                write(f2[0:4], font=("Consolas", 13, "normal"))
                count = count + 1
                penup()
                i = i - 28
                pin_yin = lp(f2[3])
                end_word = f2[3]
        file2.close()
    # 如果接龙数目达到，接龙结束
    if count == 10:
        goto(180, i - 10)
        pendown()
        write("接龙结束", font=("Consolas", 15, "normal"))
        penup()
