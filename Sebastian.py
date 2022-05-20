#funcion retornar colas fifo (first in criaturas pasivas) y (first out criaturas hostiles) aleatorias "cada que se utilice la funcion debe llamar criaturas distintas#
from collections import deque



creaturas_hostil=["escorpion gigante", "ogro", "bruja"]
colacreaturas = deque(creaturas_hostil)
print(colacreaturas)
colacreaturas.appendleft("Tortuga")
print(colacreaturas)






#x:creatura_pasiva
#y:creatura_hostil

#def retornar(creatura_pasiva_o_creatura_hostil):x,y
    #queue.enque(x,y)
     # print x
      #  queue.deque(y)
      #print y
  
