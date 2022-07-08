import numpy as np
rut=[]
pasaje=[]
compra=[rut,pasaje]
asientos_comu=0
asientos_re=0
asientos_no_r=0
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
    asientos_normal=np.ones([6,33],dtype="int")
    for i in range(6):
        for e in range(33):
            asientos_normal[i][e]=asientos_normal[i][e]*acum
            acum=acum+1
            if acum==34:
                acum=1
    asientos_normal_str=asientos_normal.astype(str)
    asientos_normal_cal=asientos_normal.astype(str)
    acum=0
    for i in range(6):
        for e in range(33):
            acum=acum+1
            if acum>=0 and acum < 34:
                asientos_normal_str[i][e]= "A"+asientos_normal_str[i][e]
            elif acum>32 and acum < 65:
                asientos_normal_str[i][e]= "B"+asientos_normal_str[i][e]
            elif acum>63 and acum <100:
                asientos_normal_str[i][e]= "C"+asientos_normal_str[i][e]
            elif acum>98 and acum <133:
                asientos_normal_str[i][e]= "D"+asientos_normal_str[i][e]
            elif acum>131 and acum <166:
                asientos_normal_str[i][e]= "E"+asientos_normal_str[i][e]
            elif acum>164 and acum <199:
                asientos_normal_str[i][e]= "F"+asientos_normal_str[i][e]
    return(asientos_normal_str,asientos_normal_cal,asientos_normal)
asientos_str,asientos_cal,asientos_num=array()
def asientos_disponibles(asientos):
    tabla=""
    acum=0
    acum_avi=0
    for i in range(6):
        for e in range(33):
            acum_avi=acum_avi+1
            acum=acum+1
            tabla= tabla +" " + asientos[i][e]
            if acum==33:
                
                tabla=tabla + "\n"
                acum=0
            if acum_avi==99:
                tabla=tabla + "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "  + "\n"
    print(tabla)
def venta(asientos,asientos_n,asientos_num,rutx,pasajex,asientos_comun,asientos_rec,asientos_no_re):
    asientos_disponibles(asientos)
    asiento_con=input("que asiento decea comprar?")
    asiento_n_upper=asiento_con.upper()
    while True:
        if asiento_n_upper in asientos:
            break
        else:
            asiento_con=input("insique una siento valido")
            asiento_n_upper=asiento_con.upper()
    result=np.where(asientos==asiento_n_upper)
    print(result)
    if (asientos_num[result]>=0 and asientos_num[result]<=5) or (asientos_num[result]==18):
        print("Su pasaje tiene un valor de 80.000 pesos")
        asientos_rec=asientos_rec+1
        print(asientos_rec)
        rutxx=input("Indique su rut")
        while True:
            if rutxx.isnumeric() and len(rutxx)<10:
                break
            else:
                rutxx=input("Indique un rut valido")
        rutx.extend([rutxx])
        pasajex.extend([asiento_n_upper])
        asientos[result]="X "
        input("la operacion se realizo con exito\npresione enter para continuar......")
    elif (asientos_num[result]>=6 and asientos_num[result]<=9) or (asientos_num[result]>=19 and asientos_num[result]<=33):
        print ("Su pasaje tiene un valor de 60.000 pesos")
        asientos_comun=asientos_comun+1
        print(asientos_comun)
        rutxx=input("Indique su rut")
        while True:
            if rutxx.isnumeric() and len(rutxx)<10:
                break
            else:
                rutxx=input("Indique un rut valido")
        rutx.extend([rutxx])
        pasajex.extend([asiento_n_upper])
        asientos[result]="X "
        input("la operacion se realizo con exito\npresione enter para continuar......")
    elif (asientos_num[result]>=10 and asientos_num[result]<=17):
        print ("Su pasaje tiene un valor de 50.000 pesos")
        asientos_no_re=asientos_no_re+1
        print(asientos_no_re)
        rutxx=input("Indique su rut")
        while True:
            if rutxx.isnumeric() and len(rutxx)<10:
                break
            else:
                rutxx=input("Indique un rut valido")
        rutx.extend([rutxx])
        pasajex.extend([asiento_n_upper])
        asientos[result]="X "
        input("la operacion se realizo con exito\npresione enter para continuar......")
    return(asientos_no_re,asientos_comun,asientos_rec)

def compras(comp,rux):
    a=len(rut)
    print ("compras que se realizaron son:")
    for i in range(a):
        print(f"Rut: {comp[0][i]} asiento {comp[1][i]}")
def busqueda(ruts,compr):
    rut=input("indique el rut que esta buscando")
    while True:
        if rut in ruts:
            break
        else:
            rut=input("indique un rut valido")
    ubi=ruts.index(rut)
    input(f"asiento comprado: {compr[1][ubi]}")
def Reasignar(ruts,compr):
    rut=input("indique el rut que esta buscando")
    while True:
        if rut in ruts:
            break
        else:
            rut=input("indique un rut valido")
    ubi=ruts.index(rut)
    input(f"asiento comprado que reasignara es: {compr[1][ubi]}")
    rutxx=input("el rut de reasignacion: ")
    while True:
        if rutxx.isnumeric() and len(rutxx)<10:
            compr[0][ubi]=rutxx
            print(f"Rut: {compr[0][ubi]} asiento {compr[1][ubi]}")
            break
        else:
            rutxx=input("Indique un rut valido") 
def calculo(asiento_barat,asiento_car,asientos_no_r):
    a=asiento_barat*50000
    b=asientos_no_r*60000
    c=asiento_car*80000
    print("------asientos-----precio------cantidad-----------total")
    print(f"asiento no reclina:-50.000------{asiento_barat}-----------{asiento_barat*50000} ")
    print(f"asiento no comun:---60.000------{asientos_no_r}-----------{asientos_no_r*60000}")
    print(f"asiento no comun:---80.000------{asiento_car}-----------{asiento_car*80000}")
    print(f"total:--------------------------{asiento_car+asientos_no_r+asiento_barat}-----------{a+b+c}")

while True:
    print(asientos_no_r,asientos_re,asientos_comu)
    print(len(rut))
    try:
        a=menu()
    except:
        print("indique un valor valido")
        input("presione enter para continuar")
        a=0
    if a==1:
        asientos_no_r,asientos_comu,asientos_re=venta(asientos_str,asientos_cal,asientos_num,rut,pasaje,asientos_comu,asientos_re,asientos_no_r)
    if a==2:
        asientos_disponibles(asientos_str)
    if a==3:
        compras(compra,rut)
    if a==4:
        busqueda(rut,compra)
    if a==5:
        Reasignar(rut,compra)
    if a==6:
        calculo(asientos_no_r, asientos_re, asientos_comu)