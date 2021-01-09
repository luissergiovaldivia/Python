def participante(ciclistas):
	
		ciclista = input('Ingresar nombre del ciclista: ')
		

		

		ciclistas.append(ciclista)
		

		while ciclista != ' ':
				ciclista = input('Ingresar nombre del ciclista: ')
				if ciclista == '':
					break

				
				ciclistas.append(ciclista)
				
		return
		


		return (ciclistas)

def carga_de_tiempo(alumnos, tiempos,tiempos_totales):
	
	dato = 0
	tiempos_total = 0


	for i in range(len(alumnos)):
		tiempos.append( [0] * 5 )


	print(tiempos)
	for i in range(len(alumnos)):
		print('')
		print('')
		print('Cargar el tiempo', alumnos[i])
		

		for j in range(5):
			
			dato = float(input('etapa {0}: '. format(j + 1)))
			tiempos[i][j] = dato
			
			tiempos_total += dato

		
		tiempos_totales.append(tiempos_total)
		tiempos_total = 0 
		
	return (tiempos)
			


def mejor_tiempo(ciclistas, tiempos_totales, ciclista_ganador):
	mayor = 0
	ciclista = 'no se encontro'
	mayor = tiempos_totales[0]

	for i in range(0,len(tiempos_totales)):
		
		if tiempos_totales[i] < mayor :
			mayor = tiempos_totales[i]
			ciclista_ganador = ciclistas[i]


		
	
	return	ciclista_ganador

ciclistas = []
tiempos = []
aprovado = []
tiempos_totales = []
ciclista_ganador = 'nadie'



participante(ciclistas)
carga_de_tiempo(ciclistas, tiempos, tiempos_totales)
mejor_tiempo(ciclistas, tiempos_totales,ciclista_ganador)


print('')

print('Los ciclistas anotados son: ')
print(ciclistas)
print('')
print(tiempos)
print('')
print(tiempos_totales)
print('')

print('El mejor tiempo lo tiene: ' ,mejor_tiempo(ciclistas, tiempos_totales, ciclista_ganador))

