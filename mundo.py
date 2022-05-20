import time as t

matriz = [['▢' for columna in range(0,32)]for fila in range(0,32)]
#creacion de mundo vacio

print("Creando mundo, por favor espere... \n")
t.sleep(2)
for fila in matriz:
  print (' '.join(map(str, fila)))
print("\n Mundo Creado Exitosamente \n")



#definicion de las coordenadas
posicionesx = []
posicionesy = []
ancho = []
alto = []

#solicitar al usuario que ingrese los datos
murosacrear = random.randint(1,5)#int(input("Cuantos muros desea crear? \n"))

for muro in range(0,murosacrear):
    valorposx = int(input(f"digite el valor de la posicion en x para el muro {muro+1} \n"))
    if valorposx == None:
      print("Digite un valor correcto")
    else:
      posicionesx.append(valorposx-1)

for muro in range(0,murosacrear):
    valorposy = int(input(f"digite el valor de la posicion en y para el muro {muro+1} \n"))
    if valorposy == None:
      print("Digite un valor correcto")
    else:
      posicionesy.append(valorposy-1)

for muro in range(0,murosacrear):
    valorancho = int(input(f"digite el valor del ancho para el muro {muro+1} \n"))
    if valorancho == None:
      print("Digite un valor correcto")
    else:
      ancho.append(valorancho)

for muro in range(0,murosacrear):
    valoralto = 0
    valoralto = int(input(f"digite el valor del alto para el muro {muro+1} \n"))
    if valoralto == None:
      print("Digite un valor correcto")
    else:
      alto.append(valoralto)
#contar la cantidad de muros a construir
muros = len(posicionesx)-1

#funcion que crea el muro, tomando coordenadas, ancho y alto
def crearmuro(posx,posy,ancho,alto):
    for fila in range(abs(alto)):
        iniciomuroy = fila+posx
        matriz[iniciomuroy][posy] = '▣'
        for columna in range(abs(ancho)):
            iniciomurox = columna+posy
            matriz[iniciomuroy][iniciomurox] = '▣'
print("Creando los muros, no tardaremos :D ...\n")
t.sleep(3)

#Ejecutar la creacion de muros para cada uno de los datos ingresados
while muros >= 0:
    crearmuro(posicionesx[muros],posicionesy[muros],ancho[muros],alto[muros])
    muros -= 1

#mostrar en pantalla la matriz con el resultado de los muros creados
print("mundo manual \n")
for fila in matriz:
    print (' '.join(map(str,fila)))



print("\n !! Los muros se han creado correctamente !! ʕ•ᴥ•ʔ ♪ ♫  \n")