from random import random
from math import floor

def xrandom():
	numero = 0
	numero_uno = 0
	numero_dos = 0
	final = 0
	#opcion = ''
	while not (numero_uno >= 1 and numero_uno <= 6):
		numero = random() 
		numero_uno = floor(numero * 6)

	#numero = random()
	#numero_dos = numero * 10
	#final = numero_uno - numero_dos
		if not (numero_uno >= 1 and numero_uno <= 6):
			numero_uno = 0
		pass
	

	return numero_uno

#numero = 0
#while (1):
accion = xrandom()

print('                                     ')
print('***************************************')
print('** El numero es ', accion,         ' **')
print('***************************************')

print('                                     ')
print('**************************************')
print('**         Muchas Gracias           **')
print('**************************************')

#		pass