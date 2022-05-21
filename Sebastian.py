#funcion retornar colas fifo (first in criaturas pasivas) y (first out criaturas hostiles) aleatorias "cada que se utilice la funcion debe llamar criaturas distintas
from collections import deque
import random

creaturas_hostil=["escorpion gigante", "ogro", "bruja"]
creaturas_pasiva=["ave","caballo","perro"]

def retornarcreaturashostil(creaturas_hostil:str):
  colacreaturas_hostil = deque(creaturas_hostil)
  print (colacreaturas_hostil)
  colacreaturas_hostil.appendleft.randomchoise("zombie""troll""gigante")
  print (colacreaturas_hostil)

def retornarcreaturaspasivas(creaturas_pasiva:str):
  colacreturas_pasiva = deque(creaturas_pasiva)
  print(colacreaturas_pasiva)
  colacreturas_pasiva.appendleft.ramdonchoise("tortuga""conejo""pez")
  print(colacreaturas_pasiva)

  
  #################################################################################
  
def criaturaspasivas(numerocriaturaspasivas):
  colacriaturaspasivas = deque()
  for x in range(numerocriaturaspasivas):
    criaturaspasivas=["ave""parro""gato""gallina""caballo""delfin""pez""vaca""buey""siervo""gallo""mono""pato""ganzo""ardilla""panda""camello""loro""buffalo""colibri""cabra""oveja""castor""iguana""koala""conejo""tortuga""armadillo""llama""alcon"]
    random.suffle(criaturaspasivas)
    colacriaturaspasivas.append(criaturaspasivas[x])
    return colacriaturaspasivas

def criaturashostiles(numerocriaturashostiles):
  colacriaturashostiles= deque()
  for y in range(numerocriaturashostiles):
    criaturashostiles=["zombie""bruja""gigante""dinosaurio""quimera""troll""ogro""oso""gorila""mago""avestruz""leon""rinoceronte""cobra""tigre de bengala""babuino""jaguar""piraña""tiburon""aguila""lagarto""escorpion gigante""robot""cangrejo""toro""lobo""ciclope""hiena""murcielago"]
    random.shuffle(criaturashostiles)
    colacriaturashostiles.append(criaturashostiles[y])
  return colacriaturashostiles



def  generarcriaturas(numerocriaturaspasivas,numerocriaturashostiles):
  if(numerocriaturaspasivas+)

    
    
      



  
  







