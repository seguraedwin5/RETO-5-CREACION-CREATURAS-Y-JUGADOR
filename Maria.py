""""
Esta función se encarga de obtener criaturas pasivas y hostiles para que aparezcan en el juego, cada criatura debe tener los siguientes datos:
• Tipo (Pasiva / Hostil)
• Nombre
• símbolo (carácter que lo representa)
• Fila donde debe aparecer (generada aleatoriamente)
• Columna donde debe aparecer (generada aleatoriamente)
• Fecha y hora en la que aparece (tomada del sistema)"
"""

from collections import namedtuple
import random as r
import datetime as dt

contcreatura = 0

Creatura = namedtuple(
  'Creatura',
  ['Tipo', 'Nombre', 'Simbolo', 'Fila', 'Columna', 'FechayHoraAparicion'])

#definir una variable con if para hacer las colas con las tuplas
#Creacion creatura hostil
def ObtenerCreaturaHostil():  #pendiente parametro cola
    global contcreatura
    contcreatura += 1
    _tipo = 'Hostil'
    _nombre = "Creatura" + str(contcreatura)
    _simbolo = '🦂'
    _fila = r.randint(1, 17)
    _columna = r.randint(1, 17)
    _fechahoraaparicion = dt.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    return Creatura(_tipo, _nombre, _simbolo, _fila, _columna, _fechahoraaparicion)

#Creacion creatura pasiva
def ObtenerCreaturaPasiva():  #pendiente parametro cola
    global contcreatura
    contcreatura += 1
    _tipo = 'Pasiva'
    _nombre = "Creatura" + str(contcreatura)
    _simbolo = '🐥'
    _fila = r.randint(1, 17)
    _columna = r.randint(1, 17)
    _fechahoraaparicion = dt.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    return Creatura(_tipo, _nombre, _simbolo, _fila, _columna, _fechahoraaparicion)
