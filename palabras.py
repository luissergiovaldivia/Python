cadena = input('Escribe una frase: ')

while cadena != '':
		blanco = 0
		for caracter in cadena:
				if caracter == ' ':
					blanco += 1

		palabras = blanco + 1 # Hay una palabra mas que blanco

		print('Palabras:', palabras)

		cadena = input('Escriba una frase: ')


print('muchas gracias fin de programa')