filas = 10
columnas = 10
#pulso = 6

tablero = []

for i in range (filas):
	tablero.append([False]*columnas)


tablero[4][5] = True
tablero[5][5] = True
tablero[6][5] = True



#Representar tablero 
print('Estado Inicial')

for x in range(filas):
	for y in range(columnas):
		if tablero[x][y]:
			print('*', end='')
		else:
			print('.', end='')
	print()	

pulso = 6

for t in range(pulso):
	#Prepara el nuevo tablero

	nuevo = []

	for i in range(filas):
		nuevo.append([False]*columnas)

	#Actualizar el tablero
	for x in range(filas):
		for y in range(columnas):
			#calcular el numero de vecinos de la celda que estamos visitando
			# Calcular el numero de vacinos

			n = 0
			if x > 0 and y > 0 and tablero[x-1][y-1]:
				n +=1
			if y > 0 and tablero[x][y-1]:
				n +=1
			if x < filas-1 and y > 0 and tablero[x+1][y-1]:
				n +=1
			if x > 0 and tablero[x-1][y]:
				n +=1
			if x < filas - 1 and tablero[x+1][y]:
				n +=1
			if x > 0 and y < columnas - 1 and tablero[x-1][y+1]:
				n +=1
			if y < columnas - 1 and tablero[x][y+1]:
				n +=1
			if x < filas -1 and y < columnas -1 and tablero[x+1][y+1]:
				n +=1


			#Aplicar reglas

			if tablero[x][y] and (n == 2 or n == 3):#Supervivencia 
					tablero[x][y] = True
			elif not tablero[x][y] and n == 3: #Nacimiento
					tablero[x][y] = True
			else: #Superpoblacion
				tablero[x][y] = False

	print('pulso',t+1)


	for x in range(filas):
		for y in range(columnas):
			if tablero[x][y]:
				print('*', end='')
			else:
				print('.', end='')
		print()		


	




