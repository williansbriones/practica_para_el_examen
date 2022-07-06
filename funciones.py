def menu():
    try:
        accion=int(input("Que desea realizar\n 1) Comprar pasajes\n 2) Mostrar ubicaciones disponibles\n 3) Ver listado de pasajeros\n 4) Buscar pasajero 5) Reasignar asiento\n 6) Mostrar ganancias totales"))
        while accion<1 or accion>6:
            accion=int(input("Indique una accion correcta\n 1) Comprar pasajes\n 2) Mostrar ubicaciones disponibles\n3) Ver listado de pasajeros\n 4) Buscar pasajero 5) Reasignar asiento\n 6) Mostrar ganancias totales"))

    except:
        print("indique un valor valido")
    return(accion)

a=menu()
