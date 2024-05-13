def fecha ():
    fecha = int(input("Ingrese una fecha en el formato DDMMAAAA") [0:8])
    año = fecha % 10000
    fecha = int (fecha / 10000)
    mes = fecha % 100
    fecha = int (fecha / 100)
    dia = fecha

    print ("el dia va ser: " , dia ,"el mes va ser: ", mes,"el año va ser: ", año)

fecha ()
