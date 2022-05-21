import pprint  #esta libreria se usa para imprimir diccionarios en filas separadas
#import Erica as Er
import Edwin as E
import Maria as M
import Cola as c
#import Sebastian as S
#import mundo

#----------------------------------
#--------- Codigo Erica -----------

#------ Codigo Edwin ---------------
#import Yesid as Y
#------ Codigo Yesid ---------------
#---- Creacion del jugador ---------

colahostiles = c.ColaCreaturas()
colahostiles.Encolar("Raton")
colahostiles.Encolar("Escopion")


if(colahostiles.EstaVacia()):
    print("La cola esta vacia \n")
else:
    print("la cola no esta vacia")

colahostiles.MostrarCola()
print(colahostiles.ContarItems())
jugador = E.ObtenerJugador("Maria")
pprint.pprint(jugador._asdict())
print('\n')
#----------------------------------
#--------- Codigo Maria -----------
chostil = M.ObtenerCreaturaHostil()
pprint.pprint(chostil._asdict())
print('\n')
cpasiva = M.ObtenerCreaturaPasiva()
pprint.pprint(cpasiva._asdict())
print('\n')
chostil2 = M.ObtenerCreaturaHostil()
pprint.pprint(chostil2._asdict())
print('\n')
