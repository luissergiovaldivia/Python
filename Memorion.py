from random import randrange
from turtle import Screen , Turtle
from time import sleep

CeldaCerrada = 0
CeldaAbierta = 1
CeldaTemporalmenteAbierta = 2

def crear_matriz(filas, columnas):
	matriz = []
	for i in range(filas):
		matriz.append([None] * columnas)
	return matriz


def rellena_simbolos(simbolo): #Tercera version
		numsimbolo = 0
	
		for i in range(len(simbolo)) :
			for j in range(len(simbolo[0])):
				simbolo[i][j] = chr(ord('a') + numsimbolo //2)
				numsimbolo += 1

		for i in range(1000):
			[f1, c1] = [randrange(len(simbolo)), randrange(len(simbolo[0]))]
			[f2, c2] = [randrange(len(simbolo)), randrange(len(simbolo[0]))]
			tmp = simbolo[f1][c1]
			simbolo[f1][c1] = simbolo[f2][c2]
			simbolo[f2][c2] = tmp


"""				ocupado = True
				while ocupado:
					[i, j] = [randrange(len(simbolo)), randrange(len(simbolo[0]))]

					if simbolo[i],[j] == None:
						ocupado = False

					simbolo[i][j] = caracter """	

def inicializar_tablero(tablero):
	for i in range(len(tablero)):
		for j in range(len(tablero[0])):
			tablero[i][j] = CeldaCerrada

def dibuja_tablero(tablero, simbolo):
	for i in range(len(simbolo)):
		for j in range(len(simbolo[0])):
			dibuja_celda(tablero, simbolo, i, j)

def dibuja_celda(baldosa, simbolo, i, j):
	global tortuga
	tortuga.penup()
	tortuga.goto(j+5, i)
	tortuga.begin_fill()
	if baldosa[i][j] == CeldaCerrada:
		tortuga.fillcolor('blue')
		tortuga.circle(.5)
	elif baldosa[i][j] == CeldaAbierta:
		tortuga.fillcolor('white')
		tablero.circle(5)
		tablero.goto(j+.5, i+.25)
		tortuga.write(simbolo[i][j])
	else:
		tortuga.fillcolor('yellow')
		tortuga.circle(.5)
		tortuga.goto(j+.5, i+.25)
		tortuga.write(simbolo[i][j])

	tortuga.end_fill()
	tortuga.pendown()


def clic(x, y):
	global tablero, simbolo, temporal1, temporal2
	print(x, y)
	[j, i] = [int(x), int(y)]
	print('')
	print([i, j])
	print('paso 1')
	print([len(simbolo), len(simbolo[0])])
	if 0 <= i < len(simbolo) and 0 <= j < len(simbolo[0]):
		print('paso 2')
		if tablero[i][j] == CeldaCerrada:
			print('paso 3')

			if temporal1 == None:
				print('paso 4')
				temporal1 = [i, j]
				tablero[i][j] = CeldaTemporalmenteAbierta
				print('temporal1: ', temporal1)
				print('tablero:', tablero[i][j])
			else:
				print('paso 5')
				temporal2 = [i, j]

				tablero[i][j] = CeldaTemporalmenteAbierta

			dibuja_celda(tablero, simbolo, i, j)
			print('paso 6')

			if temporal2 != None:
				print('paso 7')
				if simbolo[temporal1[0]][temporal1[1]] == simbolo[temporal2[0]][temporal2[1]]:
					print('paso 8')
					tablero[temporal1[0]][temporal1[1]] = CeldaAbierta
					tablero[temporal2[0]][temporal2[1]] = CeldaAbierta

				else:
					print('paso 9')
					sleep(0.5)
					tablero[temporal1[0]][temporal1[1]] = CeldaCerrada
					tablero[temporal2[0]][temporal2[1]] = CeldaCerrada

				print('paso 10')
				dibuja_celda(tablero, simbolo, temporal1[0], temporal1[1])
				dibuja_celda(tablero, simbolo, temporal2[0], temporal2[1])

				temporal1 = None
				temporal2 = None

		dibuja_celda(tablero, simbolo, i, j)
		print('paso 11')
temporal1 = None
temporal2 = None



#print('Clic en fila {0} y columna {1}' . format(i, j))


		

#Programa Principal

filas = 4
columnas = 6


pantalla = Screen()
pantalla.setup(columnas*50, filas*50)
pantalla.screensize(columnas*50, filas*50)
pantalla.setworldcoordinates(-5, -5, columnas+5, filas+5)
pantalla.delay(0)
tortuga = Turtle()
tortuga.hideturtle()
simbolo = crear_matriz(filas, columnas)
tablero = crear_matriz(filas, columnas)

inicializar_tablero(tablero)
rellena_simbolos(simbolo)
dibuja_tablero(tablero,simbolo)

pantalla.onclick(clic)

#tortuga.onclick(clic)

pantalla.mainloop()


#pantalla.exitonclick()