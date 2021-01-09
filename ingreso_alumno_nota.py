def ingresar_elemento(alumnos, notas):
	
		elemento = input('Ingresar alumno: ')
		

		calificacion = int(input('Ingresar nota: '))

		alumnos.append(elemento)
		notas.append(calificacion)

		while elemento != ' ':
				elemento = input('Ingresar alumno: ')
				if elemento == '':
					break

				calificacion = int(input('Ingresar nota: '))

				alumnos.append(elemento)
				notas.append(calificacion)
		return
		#pass


		return (alumnos, notas)

alumnos = []
notas = []
ingresar_elemento(alumnos, notas)

#for i in range(0, len(alumnos)):
	#print(alumnos[i])
	#print(notas[i])

print(alumnos)
print(notas)

