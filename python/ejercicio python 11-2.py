def ejercicio11():
    moviles = []
    repeticiones = int(input("Ingrese la cantidad de autos que quiere ingresar"))
   
    for i in range(repeticiones):
         valor = float(input("Ingrese el porcentaje del valor del coche"))
         moviles.append(valor)    
   
   
    comision = repeticiones * 200
    bonus = sum(moviles) * 0.05
    sueldototal = 5500 + comision + bonus

    print("El sueldo total es de:  ", sueldototal )