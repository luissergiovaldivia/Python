from turtle import Screen, Turtle
from math import sin, pi, cos

pantalla = Screen()
pantalla.setup(825,425)
pantalla.screensize(800,400)
#pantalla.screensize(100,100)
#pantalla.setworldcoordinates(-2*pi, -1, 2*pi, 1)
#pantalla.setworldcoordinates(-10, -10, 10, 10)
pantalla.setworldcoordinates(-40, -300, 40, 300)

tortuga = Turtle()

#x = -2*pi
x = -25
a = 1
b = 2
c = 3



dx = 4*pi / 800
tortuga.pencolor('blue')
tortuga.penup()
#tortuga.goto(x, sin(x))
tortuga.goto(x, (a*x**2+b*x+c))
#tortuga.pendown()

#tortuga.goto(x, cos(x))
tortuga.pendown()

while x <= 25:
#	tortuga.goto(x, sin(x))
	#tortuga.goto(x, cos(x))
	tortuga.goto(x, (a*(x)**2+b*(-x)+c))
	x += 0.5
	#x += dx

#x = -2*pi
#tortuga.pencolor('red')
#tortuga.penup()
#tortuga.goto(x, sin(x))
#tortuga.pendown()

#tortuga.goto(x, cos(x))
#tortuga.pendown()

#while x <= 2*pi:
	#tortuga.goto(x, sin(x))
	#tortuga.goto(x, cos(x))
	#x += 0.01
	#x += dx

#tortuga.goto(-25, (a*(-25)**2+b*(-25)+c))
#tortuga.pendown()
#tortuga.goto(-10, (a*(-10)**2+b*(-10)+c))
#tortuga.pendown()
#tortuga.goto(-1.5*pi, sin(-1.5*pi))
#tortuga.goto(-8, (a*(-8)**2+b*(-8)+c))
#tortuga.goto(-1*pi, sin(-1*pi))
#tortuga.goto(-6, (a*(-6)**2+b*(-6)+c))
#tortuga.goto(-0.5*pi, sin(-0.5*pi))
#tortuga.goto(-4.5, (a*(-4.5)**2+b*(-4.5)+c))
#tortuga.goto(0, (a*(0)**2+b*(0)+c))
#tortuga.goto(0, sin(0))
#tortuga.goto(6, (a*6**2+b*6+c))
#tortuga.goto(0.5*pi, sin(0.5*pi))
#tortuga.goto(8, (a*8**2+b*8+c))
#tortuga.goto(1*pi, sin(1*pi))
#tortuga.goto(10, (a*10**2+b*10+c))
#tortuga.goto(1.5*pi, sin(1.5*pi))
tortuga.goto(25, (a*25**2+b*25+c))
#tortuga.goto(2*pi, sin(2*pi))

pantalla.exitonclick()