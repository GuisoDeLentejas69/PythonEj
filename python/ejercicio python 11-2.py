def calcular_salario_vendedor(autos_vendidos, valor_unidad):
 
    salario_base = 5500
    
    comision_por_auto = 200
    
    comision_adicional = valor_unidad * 0.05
    
    comisiones = (autos_vendidos * comision_por_auto) + (autos_vendidos * comision_adicional)
    
    salario_total = salario_base + comisiones
    
    return salario_total

autos_vendidos = int(input("Ingrese el número de autos vendidos: "))
valor_unidad = float(input("Ingrese el valor de venta de cada unidad: "))

salario_vendedor = calcular_salario_vendedor(autos_vendidos, valor_unidad)
print(f"El salario total del vendedor es: ${salario_vendedor}")