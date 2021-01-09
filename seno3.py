from turtle import Screen, Turtle
from math import sin, pi, cos

pantalla = Screen()
pantalla.setup(825,425)
pantalla.screensize(800,400)
pantalla.setworldcoordinates(-2*pi, -1, 2*pi, 1)

tortuga = Turtle()

x = -2*pi

dx = 4*pi / 800
tortuga.pencolor('blue')
tortuga.penup()
tortuga.goto(x, sin(x))
#tortuga.pendown()

#tortuga.goto(x, cos(x))
tortuga.pendown()

while x <= 2*pi:
	tortuga.goto(x, sin(x))
	#tortuga.goto(x, cos(x))
	#x += 0.01
	x += dx

x = -2*pi
tortuga.pencolor('red')
tortuga.penup()
#tortuga.goto(x, sin(x))
#tortuga.pendown()

tortuga.goto(x, cos(x))
tortuga.pendown()

while x <= 2*pi:
	#tortuga.goto(x, sin(x))
	tortuga.goto(x, cos(x))
	#x += 0.01
	x += dx


#tortuga.goto(-1.5*pi, sin(-1.5*pi))
#tortuga.goto(-1*pi, sin(-1*pi))
#tortuga.goto(-0.5*pi, sin(-0.5*pi))
#tortuga.goto(0, sin(0))
#tortuga.goto(0.5*pi, sin(0.5*pi))
#tortuga.goto(1*pi, sin(1*pi))
#tortuga.goto(1.5*pi, sin(1.5*pi))
#tortuga.goto(2*pi, sin(2*pi))

pantalla.exitonclick()