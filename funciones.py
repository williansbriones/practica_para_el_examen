import numpy as np
def menu():
    try:
        accion=int(input("Que desea realizar\n 1) Comprar pasajes\n 2) Mostrar ubicaciones disponibles\n 3) Ver listado de pasajeros\n 4) Buscar pasajero\n 5) Reasignar asiento\n 6) Mostrar ganancias totales"))
        while accion<1 or accion>6:
            accion=int(input("Indique una accion correcta\n 1) Comprar pasajes\n 2) Mostrar ubicaciones disponibles\n 3) Ver listado de pasajeros\n 4) Buscar pasajero\n 5) Reasignar asiento\n 6) Mostrar ganancias totales"))

    except:
        print("indique un valor valido")
    return(accion)
def array():
    acum=1
    asientos_normal=np.ones([6,15],dtype="int")
    print(asientos_normal)
    for i in range(6):
        for e in range(15):
            asientos_normal[i][e]=asientos_normal[i][e]*acum
            acum=acum+1
            if acum==16:
                acum=1
    print(asientos_normal)
asientos=array()
def asientos_disponibles():
    tabla
while True:
    try:
        a=menu()
    except:
        print("indique un valor valido")
        input("presione enter para continuar")
        a=0
    if a==1:
        pass
    if a==2:
        pass
    if a==3:
        pass
    if a==4:
        pass
    if a==5:
        pass
    if a==6:
        pass