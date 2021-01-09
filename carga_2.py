import pickle

#leemos la lista cargandola del fichero mifichero.mio

lista = pickle.load(open('mifichero2.mio', 'rb'))

# le mostramos en pantalla

print(lista)