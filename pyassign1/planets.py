#!/user/bin/env python3

"""Foobar.py:Description of what footbar does.

__author__ = "Weixin"
__pkuid__  = "1800011764"
__email__  = "1800011764@pku.edu.cn"
"""

import math
import turtle

wn = turtle.Screen()
wn.bgcolor('black')
Sun = turtle.Turtle()
Sun.shapesize(2)
Sun.shape('circle')
Sun.color('red')

Mercury = turtle.Turtle()
Venus = turtle.Turtle()
Earth = turtle.Turtle()
Mars = turtle.Turtle()
Jupiter = turtle.Turtle()
Saturn = turtle.Turtle()

planets = [Mercury, Venus, Earth, Mars, Jupiter, Saturn]
colors = ['purple', 'green', 'black', 'yellow', 'orange', 'blue']
ps = [300, 500, 700, 900, 1200, 1500]      # ps是行星轨道的焦准距的集合
es = [0.11, 0.12, 0.13, 0.14, 0.15, 0.16]  # es是行星轨道的离心率的集合
shapesizes = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
speeds = [5, 20, 35, 40, 40, 35]

for i in range(6):
    planet = planets[i % 6]
    planet.hideturtle()
    planet.shape('circle')
    planet.shapesize(shapesizes[i % 6])
    planet.color(colors[i % 6])
    planet.speed(0)
    p = ps[i % 6]
    e = es[i % 6]
    planet.penup()
    planet.goto(e*p/(1-e), 0)
    planet.pendown()
    planet.showturtle()

for n in range(3600):
    for m in range(6):
        planet = planets[m % 6]
        p = ps[m % 6]
        e = es[m % 6]
        n = speeds[m % 6]*math.radians(n)
        d = e*p/(1-e*math.cos(n))
        x = d*math.cos(n)
        y = d*math.sin(n)
        planet.goto(x, y)
