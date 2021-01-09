def serie(lista):
	candidato = lista[0]
	suma = 0
	cantidad = 1
	mayor = 0
	indice = 0
	for elemento in lista:

		if elemento == candidato :
			if cantidad > 1:
				indice = lista.index(elemento)

			candidato = elemento
			cantidad +=1

		else:
			suma += 1
			candidato = elemento
			if mayor < cantidad:
					mayor = cantidad
					indice_mayor = indice
					#indice = 0
			cantidad = 1
	suma += 1
	print('mayor: ', mayor)
	print('indice de la serie mas larga: ', indice_mayor)
	return suma
	

a = [1, 1, 8, 8, 8, 8, 0, 0, 0, 2, 10, 10, 10, 10, 10]

print('El numero de series es ', serie(a))
#print(serie(a))

