from turtle import Screen, Turtle

pantalla = Screen()

pantalla.setup(425,425)
pantalla.screensize(400,400)
pantalla.setworldcoordinates(-50,-150,350,250)


tortuga = Turtle()

tortuga.pensize(3)
tortuga.dot(10)
tortuga.forward(100)
tortuga.dot(10)
tortuga.forward(100)
tortuga.dot(10)
tortuga.forward(100)
tortuga.dot(10)

tortuga.penup()
tortuga.goto(0,100)
tortuga.pendown()

tortuga.pencolor('red')
tortuga.pensize(5)
tortuga.circle(20)
tortuga.forward(50)
tortuga.pensize(4)
tortuga.left(20)
tortuga.circle(20)
tortuga.forward(50)
tortuga.pensize(3)
tortuga.left(20)
tortuga.circle(20)
tortuga.forward(50)
tortuga.pensize(2)
tortuga.left(20)
tortuga.circle(20)
tortuga.forward(50)



tortuga.penup()
tortuga.goto(0,-100)
tortuga.towards(0,0)

tortuga.write('Hola.')
tortuga.backward(20)
tortuga.write('Adios.')





pantalla.exitonclick()
