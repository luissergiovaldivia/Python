def muestra_nota_de_alumno(alumnos, nota, alumno_buscado):
	encontrado = False
	for i in range(len(alumnos)):
		if alumnos[i] == alumno_buscado:
			print(alumno_buscado, nota[i])
			encontrado = True

	if not encontrado:
		print('El alumno {0} no pertenece al grupo ', format(alumno_buscado))


alumnos = ['Ana Pi', 'Pau Lopez', 'Luis Sol', 'Mar Vega', 'Paz Mir']

notas = [10, 5.5, 2.0, 8.5, 7.0]

a = muestra_nota_de_alumno(alumnos, notas, 'Sergio Valdivia')