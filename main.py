# random walk
import turtle
from turtle import *
import random

timy = Turtle()
screen = Screen()
#random color setting
turtle.colormode(255)

#random color function
def color2():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


a = True
while a:
    timy.forward(10)
    m = random.randint(0, 3)
    timy.color(color2())
    timy.width(10)
    timy.right(m * 90)
    timy.speed(10)
    timy.forward(10)
