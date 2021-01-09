def menu():
	opcion = ''
	while  not (opcion >= 'a' and opcion <= 'c'):
		print('Cajero automatico.')
		print('a) Ingresar dinero.')
		print('b) Sacar dinero.')
		print('c) Cosultar saldo.')
		opcion = input('Escoja una opcion: ')

		if not (opcion >= 'a' and opcion <= 'c'):
			print('Solo puede escoger a, b o c. Intentelo de nuevo')

		pass

	return opcion


accion = menu()

print('                                     ')
print('**************************************')
print('** Ud a seleccionado la opcion: ', accion, ' **')
print('**************************************')