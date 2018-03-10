from turtle import *

def draw_triangle(size = 120, c = 'red'):
    for i in range(3):
        color(c)
        begin_fill()
        forward(size)
        left(120)
        end_fill()


def square(size = 120):
    for i in range(4):
        color('green')
        begin
        forward(size)
        left(90)


def pentagon():
    for i in range(1):
        color('blue')
        begin_fill()
        forward(120)
        left(65)
        forward(120)
        left(80)
        forward(135)
        left(70)
        forward(135)
        left(80)
        forward(120)
        end_fill()

def hexagon(size = 120):
    for i in range(6):
        color('yellow')
        down()
        forward(size)
        left(60)


def octagon(size = 100):
    for i in range(8):
        color('orange')
        down()
        forward(size)
        left(45)


def star(size = 200):
    for i in range(5):
        color('purple')
        down()
        forward(size)
        right(144)


def draw_circle(size = 100):
    color('pink')
    down()
    width(2)
    circle(size)


