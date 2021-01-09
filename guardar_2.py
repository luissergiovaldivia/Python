import pickle

#Creamos una lista

lista = [7, 4, 10, 3]

#y ahora las guardamos en un fichero llamado mifichero.mio

pickle.dump(lista, open('mifichero2.mio', 'wb'))

