print("Programa de evaluacion de nota de alumno")

nota_alumno=input("introducir la nota del alumno:   ")

nota_alumno=int(nota_alumno)


def evaluacion (nota):
	valoracion="Aprobado"

	if nota<6:
				valoracion="Suspenso"

	return valoracion


print(evaluacion(nota_alumno))			