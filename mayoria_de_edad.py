def es_mayor_de_edad(edad):
	if edad < 18:
		resultado = False
	else:
		resultado = True

	return resultado


dato_edad = 12

resultado = es_mayor_de_edad(dato_edad)

#print('El resultado es : ', es_mayor_de_edad(23))

print('El resultado es : ', resultado)