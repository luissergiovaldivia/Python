def lee_entero_positivo():
	numero = int(input())

	while numero < 0:
		print('Ha cometido un error: El numero debe ser positivo.')
		numero = int(input())
		pass


	return numero


a = lee_entero_positivo()

print('El valor leido: ', a)