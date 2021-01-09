def suma(a,b):
		total = 0
		if a > b:
			print('el valor es 0')
			#break

		else:
			for numero in range (a, b):
				total += numero
		#break 
			return total

print('El valor de la sumatoria: ', suma(1, 5))
