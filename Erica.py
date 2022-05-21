print ("Ingresa el número de criaturas pasivas y automaticamente se agregarán las criaturas hostiles")
print ("El número de criaturas pasivas debe estar entre 0 y 50")
def criaturas():
  c=50
  pasivas = int(input("Ingresa el número de criaturas pasivas: "))
  hostiles = c-pasivas
  while pasivas in range(0,50):
    if 0 <= pasivas <= 50:
        print("El número de criaturas pasivas es:", (pasivas))
        print("El numero de criaturas hostiles es:", (hostiles))
        break
    if pasivas > 50:
        print("Número incorrecto! ingresa un valor entre 0 y 50")
    elif pasivas < 0:
        print("Número incorrecto! ingresa un valor entre 0 y 50")
    else:
        print ("El Número de criaturas pasivas es:" (pasivas), "y el Número de criaturas hostiles es:", ())
  

criaturas()                                                                                                                                                                                                                                   