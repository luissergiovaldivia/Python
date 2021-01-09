def maximo(lista):
	candidato = 0
	for elemento in lista:
		if elemento > candidato :
			candidato = elemento

	return candidato

a = [6, 2, 7, 1, 10, 1, 0]

print('El maximo es ')
print(maximo(a))