def es_perfecto(n):		#Averigua si el numero n es o no es perfecto
		sumatoria = 0
		for i in range(1, n):
			if n % i == 0:
				sumatoria += i

		return sumatoria == n


def tabla_perfecto(m):			#Muestra todos los numeros  perfectos entre 1 y m
	for i in range(1, m+1):
		if es_perfecto(i):
			print(i, 'es un numero perfecto')

numero = int(input('Dame un numero: ')) 
tabla_perfecto(numero)