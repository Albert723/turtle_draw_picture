#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Yihao Wu

import turtle
import math
import time

def hart_arc():
    '''画心形圆弧'''
    for i in range(200):
        turtle.right(1)
        turtle.forward(3)

def move_pen_position(x,y):
    '''移动画笔位置'''
    turtle.hideturtle() #隐藏画笔
    turtle.up() #提笔
    turtle.goto(x,y) #移动画笔到指定起始坐标（窗口中心为0,0）
    turtle.down() #下笔
    turtle.showturtle() #显示画笔

def draw_main():
    '''绘制爱心主体部分    '''
    # 初始化
    turtle.setup(width=1200, height=750)  # 画布大小
    turtle.color('pink', 'pink')  # 画笔颜色
    turtle.pensize(5)  # 画笔粗细
    turtle.speed(1)  # 画笔速度

    # 初始化画笔起始坐标
    move_pen_position(x=0, y=-270)  # 移动画笔位置
    turtle.left(140)  # 向左旋转140度
    turtle.begin_fill()  # 标记背景填充位置
    # 画心形直线（ 左下方 ）
    turtle.forward(336)  # 向前移动画笔，长度为224

    # 画爱心圆弧
    turtle.speed(0)  # 圆弧速度绘制过慢，此时加快速度
    hart_arc()  # 左侧圆弧
    turtle.left(120)  # 调整画笔角度
    hart_arc()  # 右侧圆弧

    # 画心形直线（ 右下方 ）
    turtle.speed(1)  # 画笔速度
    turtle.forward(336)
    time.sleep(0.8)
    turtle.end_fill()  # 标记背景填充结束位置
    # 在心形中写上表白话语
    move_pen_position(0, 0)  # 表白语位置
    turtle.hideturtle()  # 隐藏画笔
    turtle.color('#CD5C5C', 'black')  # 字体颜色
    time.sleep(0.5)
    # font:设定字体、尺寸（电脑下存在的字体都可设置） align:中心对齐
    turtle.write(love, font=('times new roman', 30, 'bold'), align="center")

def draw_signature():
    '''签写署名'''
    if signature != '':
        turtle.color('red', 'blue')
        time.sleep(0.2)
        move_pen_position(270, -270)
        turtle.hideturtle()  # 隐藏画笔
        turtle.write(signature, font=('Microsoft YaHei', 20), align="center")

def draw_word(words,positionx=500,alignstyle="right"):
    '''打印加油文字'''
    turtle.color('red', 'blue')
    time.sleep(0.2)
    move_pen_position(positionx, 0)
    turtle.hideturtle()  # 隐藏画笔
    turtle.write(words, font=('KaiTi', 90), align=alignstyle)

def draw_n_angle(turtle, size=50, num=5, color=None):
    ''' 绘制正n角形，默认为黄色
    args:
        turtle: turtle对象实例
        size: int类型，正多角形的边长
        n: int类型，是几角形
        color: str， 图形颜色，默认不填色
    '''
    if color:
        turtle.begin_fill()
        turtle.fillcolor(color)
    for i in range(num):
        turtle.forward(size)
        turtle.left(360.0 / num)
        turtle.forward(size)
        turtle.right(2 * 360.0 / num)
    if color:
        turtle.end_fill()

def draw_5_angle(turtle=None, start_pos=(0, 0), end_pos=(0, 10), radius=120, color=None):
    ''' 根据起始位置、结束位置和外接圆半径画五角星
    args:
        turtle: turtle对象实例
        start_pos: int的二元tuple，要画的五角星的外接圆圆心
        end_pos: int的二元tuple，圆心指向的位置坐标点
        radius: 五角星外接圆半径
        color: str， 图形颜色，默认不填色
    '''
    turtle = turtle or turtle.Turtle()
    size = radius * math.sin(math.pi / 5) / math.sin(math.pi * 3 / 10)
    angle = math.degrees(math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0]))
    print(angle)
    turtle.penup()
    turtle.goto(start_pos)
    turtle.setheading(0)
    turtle.left(angle)
    turtle.fd(radius)
    turtle.pendown()
    turtle.right(math.degrees(math.pi * 9 / 10))
    draw_n_angle(turtle, size, 5, color)

def draw_flag():
    large1 = 1.18  # 国旗面放大倍数
    large = 1  # 五角星放大倍数与位置变换
    # 绘制五星红旗,默认规格为30*20
    width, height = 300*large1, 200*large1
    # 初始化屏幕和海龟
    # window = turtle.Screen()
    # turtle = turtle.Turtle()
    #turtle.reset()# 恢复所有设置且清除之前图案
    turtle.pensize(1)
    turtle.color("red")
    degree = 0
    turtle.setheading(degree)#海龟朝向，degree代表角度
    turtle.hideturtle()
    turtle.speed(10)
    # 画红旗
    turtle.penup()
    turtle.goto(-300*large1 / 2, 200*large1 / 2) #重新定位画笔起点
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('red')
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(height)
    turtle.right(90)
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(height)
    turtle.right(90)
    turtle.end_fill()
    # 画大星星
    draw_5_angle(turtle, start_pos=(-100*large, 50*large), end_pos=(-100*large, 80*large), radius=30, color='yellow')
    # 画四个小星星
    stars_start_pos = [(-5*large, 8*large), (-3*large, 6*large), (-3*large, 3*large), (-5*large, 1*large)]
    for pos in stars_start_pos:
        draw_5_angle(turtle, start_pos=(pos[0] * 10*large, pos[1] * 10*large), end_pos=(-10 * 10*large*large, 5 * 10*large*large), radius=10,
                     color='yellow')

if __name__ == "__main__":
    love = "\n岂曰无衣，与子同袍"  # 爱心填充内容
    signature = "-----不吃辣的阿小豪"  # 默认署名
    draw_main()   #首先绘制心形框架
    time.sleep(2)
    draw_flag()   #绘制国旗
    time.sleep(0.5)
    draw_word("中国",-500,"left") #打印加油文字
    draw_word("加油")
    time.sleep(0.5)
    draw_signature() #签署名
    time.sleep(1)
    turtle.reset()
    turtle.exitonclick() # 点击关闭窗口