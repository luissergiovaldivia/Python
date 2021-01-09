from turtle import Screen, Turtle
from math import sin, pi

pantalla = Screen()
pantalla.setup(825,425)
pantalla.screensize(800,400)
pantalla.setworldcoordinates(-2*pi, -1, 2*pi, 1)

tortuga = Turtle()

x = -2*pi
tortuga.penup()
tortuga.goto(x, sin(x))
tortuga.pendown()

while x <= 2*pi:
	tortuga.goto(x, sin(x))
	x += 0.5

#tortuga.goto(-1.5*pi, sin(-1.5*pi))
#tortuga.goto(-1*pi, sin(-1*pi))
#tortuga.goto(-0.5*pi, sin(-0.5*pi))
#tortuga.goto(0, sin(0))
#tortuga.goto(0.5*pi, sin(0.5*pi))
#tortuga.goto(1*pi, sin(1*pi))
#tortuga.goto(1.5*pi, sin(1.5*pi))
#tortuga.goto(2*pi, sin(2*pi))

pantalla.exitonclick()