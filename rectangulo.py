#Programa: rectangulo.py
#Proposito: Calcula el perimetro y el area de un rectangulo a partir
#           de su altura y anchura.
# Autor: John Cleese
# Fecha: 1/01/2001


# Peticion de los datos (en metros)

altura = float(input('Dame la altura (en metros): '))
anchura = float(input('Dame la anchura (en metros):   '))


#Calculo del area y del perimetro

area=altura * anchura
perimetro = 2 * altura + 2 * anchura

#Impresion de resultado por pantalla


print ('El perimetro es de %6.2f metros' % perimetro )#solo dos decimales
print('El area es de %6.2f metros cuadrados' %area)