def sumatorio(lista):
	suma = 0
	indice1 = 1
	indice2 = 0
	maximo = 4

	for numero in range(len(lista) - 1) :
		
		
		#print('indice1 ', indice1)
		#print('indice2 ', indice2)
		#print('lista[0] ', lista[0])
		#print('lista[0] ', lista[indice1])
		#print('lista[1] ', lista[1])
		#print('lista[1] ', lista[indice2])

		valor1 = lista[indice1] - lista[indice2]
		

		suma += valor1
		#suma += 1
		
		indice1 += 1
		
		indice2 += 1

	return suma

a = [1, 3, 6, 10]


print(sumatorio(a))
