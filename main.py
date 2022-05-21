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
import pprint
import random as r
import datetime as dt
import Parte1 as p1
contcriatura = 0
listaMuros = []
listaCriaturas= []
pasivas = int(input("Ingresa el número de criaturas pasivas: "))
hostiles = int(input("Ingresa el número de criaturas hostiles: "))
Criatura = namedtuple(
  'Criatura',
  ['Tipo', 'Nombre', 'Simbolo', 'Fila', 'Columna', 'FechayHoraAparicion'])
Muro = namedtuple('Muro',['Posicionx','Posiciony','Ancho','Alto'])

Jugador = namedtuple('Jugador',['Tipo','Alias','Fila','Columna','FechayHoraAparicion','Vidas','simbolo'])
matriz = [['🟦' for columna in range(0,32)]for fila in range(0,32)]
#Creacion del jugador retorna tupla de jugador con el alias indicado
def ObtenerJugador(AliasJugador:str):
  _tipo = 'Jugador'
  _alias = AliasJugador
  _fila = r.randint(1,32)
  _columna = r.randint(1,32)
  _fechahoraaparicion = dt.datetime.now().strftime('%d/%m/%Y')
  _vidas = 10
  _simbolo = '🤠'
  return Jugador(_tipo,_alias,_fila,_columna,_fechahoraaparicion,_vidas,_simbolo)

#definir una variable con if para hacer las colas con las tuplas
#Creacion criatura hostil
chostiles = p1.Validarcriaturas(pasivas,hostiles)
colahostiles = p1.criaturashostiles(hostiles)
colapasivas = p1.criaturaspasivas(pasivas)
murosacrear = r.randint(5,10)
  
def ObtenerCriaturaHostil(nombrecriaturah:str):  #pendiente parametro cola
    global contcriatura
    contcriatura += 1
    _tipo = 'Hostil'
    _nombre = f"Criatura {str(contcriatura)} : {nombrecriaturah}" 
    _simbolo = r.choice(['🐀','🦂','🦟','🦇','🦑','🦖','🐍','🐛','🦠','🦈'])
    _fila = r.randint(1, 31)
    _columna = r.randint(1, 31)
    _fechahoraaparicion = dt.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    return Criatura(_tipo, _nombre, _simbolo, _fila, _columna, _fechahoraaparicion)

#Creacion criatura pasiva
def ObtenerCriaturaPasiva(nombrecriaturap:str):  #pendiente parametro cola
    global contcriatura
    contcriatura += 1
    _tipo = 'Pasiva'
    _nombre = f"Criatura {str(contcriatura)} : {nombrecriaturap}"
    _simbolo = r.choice(['🐥','🐱','🐼','🐶','🐠','🐴','🦘','🐺','🦢','🦆'])
    _fila = r.randint(1, 31)
    _columna = r.randint(1, 31)
    _fechahoraaparicion = dt.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    return Criatura(_tipo, _nombre, _simbolo, _fila, _columna, _fechahoraaparicion)

def crearmuro():
  _posicionx = r.randint(1,25)
  _posiciony = r.randint(1,25)
  _ancho = r.randint(1,5)
  _alto = r.randint(1,5)
  return Muro(_posicionx,_posiciony,_ancho,_alto)

def creaciondemuros(datosmuro:Muro):
    for fila in range(abs(datosmuro.Alto)):
        iniciomuroy = fila+datosmuro.Posicionx
        matriz[iniciomuroy][datosmuro.Posiciony] = '🔳'
        for columna in range(abs(datosmuro.Ancho)):
            iniciomurox = columna+datosmuro.Posicionx
            matriz[iniciomuroy][iniciomurox] = '🔳'

while murosacrear >= 0:
    murocreado = crearmuro()
    creaciondemuros(murocreado)
    listaMuros.append(murocreado)
    murosacrear -= 1

jugador = ObtenerJugador("Maria")
matriz[jugador.Fila][jugador.Columna] = jugador.simbolo



for numcriaturah in range(0,len(colahostiles)):
  criaturahostil = ObtenerCriaturaHostil(str(colahostiles[numcriaturah]))
  pprint.pprint(criaturahostil._asdict())
  print("\n")
  listaCriaturas.append(criaturahostil)
  matriz[criaturahostil.Fila][criaturahostil.Columna] = criaturahostil.Simbolo

for numcriaturap in range(0,len(colapasivas)):
  criaturapasiva = ObtenerCriaturaPasiva(str(colapasivas[numcriaturap]))
  pprint.pprint(criaturapasiva._asdict())
  print("\n")
  listaCriaturas.append(criaturapasiva)
  matriz[criaturapasiva.Fila][criaturapasiva.Columna] = criaturapasiva.Simbolo
#-------------------Parte 3 --------------------------------------------
#Crear muros






  
for fila in matriz:
  print (' '.join(map(str, fila)))
print("\n Mundo Creado Exitosamente \n")

print(f"Total Muros:  {len(listaMuros)}")
print(f"Vidas del Jugador: {jugador.Vidas}")
print(f"Total Criaturas: {len(listaCriaturas)}")
