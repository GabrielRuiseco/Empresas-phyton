import sys
class Empresa:
    clientes = []

    def __init__(self, rfc, nombre, direccion, clientes=None):
        if clientes is None:
            clientes = []
        self.rfc = rfc
        self.nombre = nombre
        self.direccion = direccion
        self.clientes = clientes

    def agregar(self, c):
        self.clientes.append(c)

    def __repr__(self):
        return "Empresa rfc:%s nombre:%s direccion:%s clientes:%s" % (
            self.rfc, self.nombre, self.direccion, self.clientes)


class Cliente:
    def __init__(self, rfcc, nom, direc):
        self.rfcc = rfcc
        self.nom = nom
        self.direc = direc

    def __repr__(self):
        return "Cliente rfcc:%s nom:%s direc:%s" % (self.rfcc, self.nom, self.direc)


def menu():
    print("\nMenu de registro\n\n1) Nueva Empresa\n2) Mostrar\n3) Fin")
    x = input("\nElije una opcion: ")
    return x

opc=menu()
my_dict = ""
c = []
while opc != "3":
    if opc == "1":
        print("\nRegistre una nueva Empresa")
        rf = input("Introduce el Rfc: ")
        # if rf == "":
        #     rf = input("Ingrese un rfc valido")
        n = input("Introduce el Nombre: ")
        # if n == "":
        #     n = input("Ingrese un nombre valido")
        d = input("Introduce la Dirección: ")
        # if d == "":
        #     d = input("Ingrese una dirección valida")
        opt = ""
        clientes = []
        Empresa = Empresa(rf, n, d, clientes)
        while opt != "no":
            print("\nIntroduce un nuevo cliente")
            rfcc = input("Introduce el rfc del cliente: ")
            # if rfcc == "":
            #     rfcc = input("Ingrese un rfc valido")
            nom = input("Introduce el nombre del cliente: ")
            # if nom == "":
            #     nom = input("Ingrese un nombre valido")
            direc = input("Introduce la dirección del cliente: ")
            # if direc == "":
            #     direc = input("Ingrese una dirección valida")
            cliente = {nom: Cliente(rfcc, nom, direc)}
            Empresa.agregar(cliente)
            opt = input("\ndesea introducir un nuevo cliente?")
        else:
            my_dict = {n: Empresa}
            print(repr(my_dict))
            opc=menu()
    elif opc == "2":
        if my_dict!="":
            print(repr(my_dict))
            print("\nMenu de registro\n\n1) Nueva Empresa\n2) Mostrar\n3) Fin")
            opc = input("\nElije una opcion: ")
        else:
            print("\nNo existen registros")
            opc=menu()
else:
    print("Fin del programa")
    sys.exit()
