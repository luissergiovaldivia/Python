filas = 50
columnas = 50
#pulso = 6

tablero = []

for i in range (filas):
	tablero.append([False]*columnas)


tablero[4][15] = True
tablero[4][16] = True
tablero[4][17] = False
tablero[4][18] = False

tablero[5][15] = False
tablero[5][16] = False
tablero[5][17] = True
tablero[5][18] = False


tablero[6][15] = False
tablero[6][16] = False
tablero[6][17] = False
tablero[6][18] = True

tablero[7][15] = False
tablero[7][16] = False
tablero[7][17] = False
tablero[7][18] = True


tablero[8][15] = False
tablero[8][16] = False
tablero[8][17] = False
tablero[8][18] = True


tablero[9][15] = False
tablero[9][16] = False
tablero[9][17] = True
tablero[9][18] = False


tablero[10][15] = True
tablero[10][16] = True
tablero[10][17] = False
tablero[10][18] = False





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
					nuevo[x][y] = True
			elif not tablero[x][y] and n == 3: #Nacimiento
					nuevo[x][y] = True
			else: #Superpoblacion
				nuevo[x][y] = False

	tablero = nuevo			
	print('pulso',t+1)


	for x in range(filas):
		for y in range(columnas):
			if tablero[x][y]:
				print('*', end='')
			else:
				print('.', end='')
		print()		


	




