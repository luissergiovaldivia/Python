def menu():
	opcion = ''
	while  not (opcion == 'si' or opcion == 's' or opcion == 'SI' or opcion == 'Si' or opcion == 'no' or opcion == 'no' or opcion == 'NO' or opcion == 'No' ):
		print('Decea realizar la transaccion.')
		#print('a) Ingresar dinero.')
		#print('b) Sacar dinero.')
		#print('c) Cosultar saldo.')
		opcion = input('Escoja una opcion: ')

		if not (opcion == 'si' or opcion == 's' or opcion == 'SI' or opcion == 'Si' or opcion == 'no' or opcion == 'n' or opcion == 'NO' or opcion == 'No'):
			print('Solo puede escoger si, s, Si, SI o no, n, No, NO. Intentelo de nuevo')

		pass

	return opcion


accion = menu()

print('                                     ')
print('***************************************')
print('** Ud a seleccionado la opcion: ', accion, ' **')
print('***************************************')

print('                                     ')
print('**************************************')
print('**         Muchas Gracias           **')
print('**************************************')