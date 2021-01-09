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

def aprovados(alumnos, notas):
	for i in range(0,len(notas)):
		if notas[i]>= 7:
			aprovado.append(alumnos[i])
	return		

alumnos = []
notas = []
aprovado = []

ingresar_elemento(alumnos, notas)

#for i in range(0, len(alumnos)):
	#print(alumnos[i])
	#print(notas[i])

print('')
print('Alumnos con notas')
print(alumnos)
print(notas)
print('')

aprovados(alumnos, notas)
print('')
print('Alumnos aprovados')
print(aprovado)
