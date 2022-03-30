from pypinyin import lazy_pinyin as lp
from turtle import *

# def search(f):
#     with open('chengyu_utf8.txt.txt', "r") as file:
#         f = file.readline()
i = 200
penup()
goto(200, i)
for x in range(10):
    pendown()
    write("见缝插针", font=("JatBrains Mono", 12, "normal"))
    penup()
    i = i-20
    goto(200, i)
exitonclick()
