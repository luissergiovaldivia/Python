def serie(lista):
	candidato = lista[0]
	suma = 0
	cantidad = 0
	for elemento in lista:
		if elemento == candidato :
			candidato = elemento
		else:
			suma += 1
			candidato = elemento
	suma += 1
	return suma
	

a = [1, 1, 8, 8, 8, 8, 0, 0, 0, 2, 10, 10]

print('El numero de series es ')
print(serie(a))
