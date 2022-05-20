class ColaCreaturas:
    #constructor
    def __init__(self):
        self.listacreaturas = []
    
    #Validar si la cola esta vacia
    def EstaVacia(self):
        if len(self.listacreaturas) == 0:
            return True
        else:
            return False
    
    #Agregar elemento a la cola de creaturas
    def Encolar(self, creatura):
        self.listacreaturas.insert(0,creatura)
    
    #Retirar Elemento de la cola
    def Desencolar(self):
        return self.listacreaturas.pop()
    
    #Contar Creaturas
    def ContarItems(self):
        return len(self.listacreaturas)
    
    #Mostrar Cola
    def MostrarCola(self):
        print(f"Cola: {self.listacreaturas} <------ primer Elemento")

