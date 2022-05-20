### Se debe tener una función que genere una estructura de datos similar a la pedida en el punto anterior para la criatura (¿tupla?, ¿diccionario?) que tenga los datos del jugador 
#• Tipo (Jugador)
#• Alias
#• Fila donde debe aparecer (generada aleatoriamente)
#• Columna donde debe aparecer (generada aleatoriamente)
#• Fecha y hora en la que aparece (tomada del sistema)
#• Numero de corazones (inicia con 10) Se debe implementar una función que permita:
#• Recibir como parámetro el alias del jugador
#• Retornar una estructura de datos (¿tupla?, ¿diccionario?) con la información retornada
###
from collections import namedtuple
import random as r
import datetime as dt
Jugador = namedtuple('Jugador',['Tipo','Alias','Fila','Columna','FechayHoraAparicion','Vidas','simbolo'])

#Creacion del jugador retorna tupla de jugador con el alias indicado
def ObtenerJugador(AliasJugador:str):
  _tipo = 'Jugador'
  _alias = AliasJugador
  _fila = r.randint(1,17)
  _columna = r.randint(1,17)
  _fechahoraaparicion = dt.datetime.now().strftime('%d/%m/%Y')
  _vidas = 10
  _simbolo = '🐱'
  return Jugador(_tipo,_alias,_fila,_columna,_fechahoraaparicion,_vidas,_simbolo)