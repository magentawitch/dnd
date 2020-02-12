print ("Bienvenido a tu inventario")

class Inventario:
    def __init__(self):
        self.diccionario = {}

    def consultar(self):
        return self.diccionario

    def modificar(self, item, cantidad):
        self.diccionario[item] = cantidad

    def agregar(self, item, cantidad):
        if item not in self.diccionario:
            self.diccionario[item] = cantidad
        else:
            self.diccionario[item] += cantidad

    def restar(self, item, cantidad):
        if item not in self.diccionario:
            raise Exception("No tienes este objeto en tu inventario")
        elif self.diccionario[item] < cantidad:
            raise Exception("No tienes la cantidad de este objeto\
             que quieres restar")
        else:
            self.diccionario[item] -= cantidad




inv = Inventario()
texto = input("Ingresa tu texto aqui: ")

while texto != "exit":
    print (texto)
    texto = input("Ingresa tu texto aqui: ")
    if texto == "exit":
        print ("Adios")
        break
