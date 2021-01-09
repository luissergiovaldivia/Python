def minmax(a, b, c):
	#Calcular el minimo

	if a < b :
		if a < c :
			min = a

		else:
			min = c

	else:
		if b < c :
			min = b

		else:
			min = c

	#Calcular el maximo

	if a > b :
		if a > c :
			max = a

		else:
			max = c

	else:
		if b > c:
			max = b

		else:
			max = c

	return [min, max]	
	

a = int(input('Ingrese el valor de a: '))
print('')
b = int(input('Ingrese el valor de b: '))
print('')
c = int(input('Ingrese el valor de c: '))
print('')

lista = minmax(a, b, c)

print(minmax(a, b, c))
print('')
print('El minimo es: ', lista[0])
print('')
print('El minimo es: ', lista[1])
