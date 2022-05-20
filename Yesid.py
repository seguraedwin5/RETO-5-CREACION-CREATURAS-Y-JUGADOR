###Para esta parte vamos a implementar dos funciones:
##La primera función
#• Dadas:
  #-La lista de muros
  #-La lista de criaturas en el juego
  #-La estructura con los datos del jugador
#• Dibuje en la consola el juego con muros,criaturas y jugadores
from collections import namedtuple

Muro = namedtuple('Muro1', ['fila', 'columna','ancho','largo'])
Muro1= (1,2,3,4),(5,6,7,8),(9,10,11,12)
print(Muro1)
print(Muro1.fila)
print(Muro1.columna)
print(Muro1.ancho)
print(Muro1.largo)

listacreaturas= ["creatura1,creatura2,creatura3"]
print(listacreaturas)
#mundo[jugador.fila][jugador.columna]= str(jugador.simbolo)


