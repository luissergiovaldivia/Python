cadena = input('Escribe una frase: ')

while cadena != '':
		cambios = 0

		anterior = ' '
		for caracter in cadena:
				if caracter == ' ' and anterior != ' ':
					cambios += 1
				anterior = caracter	

		palabras = cambios + 1 # Hay una palabra mas que blanco

		print('Palabras:', palabras)

		cadena = input('Escriba una frase: ')


print('muchas gracias fin de programa')