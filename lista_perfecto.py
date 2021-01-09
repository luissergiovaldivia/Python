def  es_perfecto(n):
	sumatoria = 0
	for i in range(1, n):
		if n % i == 0:
			sumatoria +=i

	if sumatoria == n:
		return True
	else:
		return False

	return

def lista_perfecto(l):
	for i in range (1, l):
		if es_perfecto(i):
			




dato = int(input('Ingrese un numero: '))

resultado = es_perfecto(dato)

print('Es un numero: ', resultado)	