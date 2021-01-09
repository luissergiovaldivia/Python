from random import random

def xrandom():
	numero = 0
	numero_uno = 0
	numero_dos = 0
	final = 0
	#opcion = ''
	numero = random() 
	numero_uno = numero * 10
	numero = random()
	numero_dos = numero * 10
	final = numero_uno - numero_dos
	return final

#numero = 0

accion = xrandom()

print('                                     ')
print('***************************************')
print('** El numero es ', accion,         ' **')
print('***************************************')

print('                                     ')
print('**************************************')
print('**         Muchas Gracias           **')
print('**************************************')