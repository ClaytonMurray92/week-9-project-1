import math
from turtle import Turtle
t = Turtle()
def drawCircle(t, center_x, center_y, radius):
    t.penup()
    t.goto(center_x + radius, center_y)
    t.pendown()
    step_distance = 2.0 * math.pi * radius / 120.0
    for _ in range(120):
        t.forward(step_distance)
        t.right(3)
drawCircle(t, 0, 0, 50)
