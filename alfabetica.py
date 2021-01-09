cadena = input('introduce una palabra : ')

caracter_anterior = ' '
menor = 0
mayor = 0
cambio = 1
longitud = len(cadena)


for i in range(1, longitud):
		if cadena[i] > caracter_anterior :
				cambio = cambio + 1
		else:
				cambio = cambio - 1	

		caracter_anterior = cadena[i]	
	#caracter[i] = caracter_anterior



if longitud == cambio:
		print('es una palabra alfabetica')

else:
		print('no es una palabra alfabetica')