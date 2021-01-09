cadena = input('introduce una palabra : ')

inversion = ''

for caracter in cadena:
	inversion = caracter + inversion

caracter_anterior = ' '
menor = 0
mayor = 0
cambio = 1
longitud = len(cadena)
diferente = 0


for i in range(1, longitud):
		if cadena[i]==inversion[i]:
				igual = 1
		else:
				diferente = 1	

		#caracter_anterior = cadena[i]	
	#caracter[i] = caracter_anterior


print('palabra ingresada : ', cadena)
print('                           ')
print('palabra invertida : ', inversion)
print('                               ')

if diferente == 0:
		print('es una palabra palindromo')

else:
		print('no es una palabra palindromo')