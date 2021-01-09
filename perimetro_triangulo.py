def perimetro(ladoA, ladoB, ladoC):
	return ladoA + ladoB + ladoC

lado_A = int(input('Ingrese el lado A: '))

lado_B = int(input('Ingrese el lado B: '))

lado_C = int(input('Ingrese el lado C: '))


print('El perimetro del triangulo: ', perimetro(lado_A, lado_B, lado_C))