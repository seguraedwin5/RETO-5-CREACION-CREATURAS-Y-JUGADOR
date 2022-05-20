import pprint  #esta libreria se usa para imprimir diccionarios en filas separadas
import Edwin as E
import Maria as M
import Sebastian as S
#import mundo
#------ Codigo Edwin ---------------
#import Yesid as Y
#------ Codigo Yesid ---------------
#---- Creacion del jugador -----

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
