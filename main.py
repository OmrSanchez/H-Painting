import turtle as t
from turtle import Turtle, Screen
import random

color_list = [(5, 12, 35), (40, 21, 16), (130, 89, 54), (202, 137, 119), (235, 211, 82), (188, 137, 161), (216, 83,
                                                                                                           67),
              (80, 6, 20), (33, 139, 65), (147, 86, 105), (193, 77, 101), (29, 87, 29), (220, 176, 210), (74, 107, 141),
              (152, 136, 65), (20, 207, 180), (12, 72, 28), (132, 158, 180), (7, 62, 139), (114, 188, 158),
              (86, 133, 173), (125, 8, 28), (18, 204, 220), (242, 204, 6), (236, 172, 164), (133, 223, 208)]

omy = Turtle()
omy.shape("arrow")
omy.hideturtle()
t.colormode(255)
omy.speed("fastest")

y = -200
for x in range(10):
    omy.teleport(x=-250)
    omy.teleport(y=y)
    y += 50
    for i in range(10):
        omy.dot(20, random.choice(color_list))
        omy.pu()
        omy.fd(50)
        omy.pd()


screen = Screen()
screen.exitonclick()
