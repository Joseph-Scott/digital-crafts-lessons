from turtle import *

def draw_triangle(size = 120, c = 'red'):
    for i in range(3):
        color(c)
        begin_fill()
        forward(size)
        left(120)
        end_fill()

draw_triangle()

mainloop()