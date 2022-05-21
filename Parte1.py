
from collections import deque
import random
print ("Ingresa el número de criaturas pasivas y automaticamente se agregarán las criaturas hostiles")
print ("El número de criaturas pasivas debe estar entre 0 y 50")

#pasivas = int(input("Ingresa el número de criaturas pasivas: "))
#hostiles = int(input("Ingresa el número de criaturas hostiles: "))

def Validarcriaturas(pasivas, hostiles):
    if pasivas + hostiles > 50:
        print("Número incorrecto! ingresa un valor entre 0 y 50")
    elif pasivas + hostiles <= 0:
        print("Digite un número mayor a 0")
    else:
        print("El número de criaturas pasivas es:", (pasivas))
        print("El numero de criaturas hostiles es:", (hostiles))
        return pasivas + hostiles
            
#funcion retornar colas fifo (first in criaturas pasivas) y (first out criaturas hostiles) aleatorias "cada que se utilice la funcion debe llamar criaturas distintas


  
  #################################################################################
  
def criaturaspasivas(pasivas):
    colacriaturaspasivas = deque()
    for x in range(pasivas):
        criaturaspasivas=["ave","parro","gato","gallina","caballo","delfin","pez","vaca","buey","siervo","gallo","mono","pato","ganzo","ardilla","panda","camello","loro","buffalo","colibri","cabra","oveja","castor","iguana","koala","conejo","tortuga","armadillo","llama","halcon"]
        random.shuffle(criaturaspasivas)
        colacriaturaspasivas.append(criaturaspasivas[x])
    return colacriaturaspasivas

def criaturashostiles(hostiles):
    colacriaturashostiles= deque()
    for y in range(hostiles):
        criaturashostiles=["zombie","bruja","gigante","dinosaurio","quimera","troll","ogro","oso","gorila","mago","avestruz","leon","rinoceronte","cobra","tigre de bengala","babuino","jaguar","piraña","tiburon","aguila","lagarto","escorpion gigante","robot","cangrejo","toro","lobo","ciclope","hiena","murcielago"]
        random.shuffle(criaturashostiles)
        colacriaturashostiles.append(criaturashostiles[y])
    return colacriaturashostiles



