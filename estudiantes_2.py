def Ingresar_estudiante(lista_estudiante, notas):
	
		estudiante = input('Ingresar nombre del estudiante: ')
		
		lista_estudiante.append(estudiante)

		calificacion =float(input('Ingresar nota: '))

		notas.append(calificacion)
		

		"""while ciclista != ' ':
				ciclista = input('Ingresar nombre del ciclista: ')
				if ciclista == '':
					break

				
				ciclistas.append(ciclista)
				
		return"""
		


		return lista_estudiante, notas

def notas(estudiante, nota,tiempos_totales):
	
	dato = 0
	tiempos_total = 0


	for i in range(len(lista_estudiante)):
		lista_notas.append( [0] * 5 )


	print(nota)
	for i in range(len(lista_estudiante)):
		print('')
		print('')
		print('Cargar la nota', lista_estudiante[i])
		

		for j in range(5):
			
			dato = float(input('etapa {0}: '. format(j + 1)))
			lista_notas[i][j] = dato
			
			tiempos_total += dato

		
		tiempos_totales.append(tiempos_total)
		tiempos_total = 0 
		
	return (lista_notas)
			


def mejor_tiempo(ciclistas, tiempos_totales, ciclista_ganador):
	mayor = 0
	ciclista = 'no se encontro'
	mayor = tiempos_totales[0]

	for i in range(0,len(tiempos_totales)):
		
		if tiempos_totales[i] < mayor :
			mayor = tiempos_totales[i]
			ciclista_ganador = ciclistas[i]


		
	
	return	ciclista_ganador


def menu():
	opcion = ''
	while  not (opcion >= '1' and opcion <= '8'):
		print('Lista de estudiantes y notas.')
		print('1) Añadir estudiante y calificacion.')
		print('2) Mostrar lista de estudiantes con sus calificaciones.')
		print('3) Calcular la media de las calificaciones.')
		print('4) Calcular el numero de aprobados.')
		print('5) Mostrar los estudiantes con mejor calificacion.')
		print('6) Mostrar los estudiantes con calificacion superior a la media.')
		print('7) Consulta la nota de un estudiante determinado.')
		print('8) FINALIZAR EJECUCION DEL PROGRAMA.')
		#print('3) Calcular la media de las calificaciones.')

		print('')	
		opcion = input('Escoja una opcion: ')
		print('')

		if not (opcion >= '1' and opcion <= '8'):
			print('Solo puede escoger a, b o c. Intentelo de nuevo')

		pass

	return opcion


def seleccion_menu(accion, lista_estudiante, notas, suma, cantidad):
	if accion == 1 :
	
		print('Usted selecciono Añadir estudiante y calificacion')
		print(' ')
		opcion = 'S'

		while opcion == 'S':

			Ingresar_estudiante(lista_estudiante, notas)
		#print(lista_estudiante)
		#print(notas)
			opcion = input('Desea seguir? (S/N): ')



	elif accion == 2:
			print('Usted selecciono Mostrar lista de estudiantes con sus calificaciones')
			print('')
			print(lista_estudiante)
			print(notas)

	elif accion == 3:
				print('Usted selecciono Calcular la media de las calificaciones')
				cantidad = len(lista_estudiante)

				for i in range(0, cantidad):
					suma = suma + notas[i]

				media = suma / cantidad
				print('La media es :', media)		

	elif accion == 4:
					print('Usted selecciono Calcular el numero de aprobados.')
					for i in range(0, cantidad):
						if notas[i] > 7:
							aprobados += 1

					print(aprobados)

	elif accion == 5:
						print('Usted selecciono Mostrar los estudiantes con mejor calificacion.')

	elif accion == 6:
							print('Usted selecciono Mostrar los estudiantes con calificacion superior a la media.')
		
	elif accion == 7:
						print('Usted selecciono Consulta la nota de un estudiante determinado.')

		
	elif accion == 8:
									print('Usted FINALIZAR EJECUCION DEL PROGRAMA.')
	return

lista_estudiante = []
estudiante = ''
notas = []
aprobado = []
tiempos_totales = []
ciclista_ganador = 'nadie'
suma = 0
cantidad = 0


while True:
	accion = int(menu())

	seleccion = seleccion_menu(accion, lista_estudiante, notas, suma, cantidad)

	print('                                     ')
	print('**************************************')
	print('** Ud a seleccionado la opcion: ', accion, ' **')
	print('**************************************')






#participante(ciclistas)
#carga_de_tiempo(ciclistas, tiempos, tiempos_totales)
#mejor_tiempo(ciclistas, tiempos_totales,ciclista_ganador)


#print('')

#print('Los ciclistas anotados son: ')
#print(ciclistas)
#print('')
#print(tiempos)
#print('')
#print(tiempos_totales)
#print('')

#print('El mejor tiempo lo tiene: ' ,mejor_tiempo(ciclistas, tiempos_totales, ciclista_ganador))

