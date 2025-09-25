class Tienda():
    def __init__(self,productos,trabajadores,ganancias):
        self.productos = productos
        self.trabajadores = trabajadores
        self.ganancias = ganancias

    def info(self):
        return f"Hay {self.trabajadores} trabajadores y quedan {self.productos} productos"

print("Cree una tienda")
productos = (input("Ingrese la cantidad de productos: "))
trabajadores = (input("Ingrese la cantidad de trabajadores: "))  

ganancia = (input("Agregar ganancia: "))
ganancia = int(ganancia)

while ganancia <= 0:
    print("No se ha podido registrar la ganancia")
    (input("Agregar ganancia: "))
    ganancia = int(ganancia)
    break

if ganancia > 0:
    print("Ganancia registrada con exito")
    

Tienda = Tienda(productos,trabajadores,ganancia)

print(Tienda.info())

## --Portada-- 
##print (" /¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\                    ________   __    _______    ____    __    ______       ______               \n"
     ##   "/                 \                  |__    __| |__|  |   ____|  |    \  |  |  |   __  \    /  __  \               \n"
     ##   "|¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨|                ^    |  |     __   |  |____   |  |\ \ |  |  |  |  \  \  |  |  |  |               \n"
     ##   "|    __ |¨¨¨¨¨¨¨¨||               / \   |  |    |  |  |   ____|  |  | \ \|  |  |  |   |  | |  |__|  |                \n"
     ##   "|   |  ||________||    o    o    /___\  |  |    |  |  |  |____   |  |  \    |  |  |__/  /  |   __   |                 \n"
     ##  "|___|__|__________|    |    |      |    |__|    |__|  |_______|  |__|   \___|  |_______/   |__|  |__| Por: JavierMGB
