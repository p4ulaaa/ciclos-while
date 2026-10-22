contador_trabajadores = 0

salario_mensual = float(input("Ingrese el salario mensual (0 para terminar): "))

while salario_mensual != 0:
    dias_trabajados = int(input("Ingrese los días trabajados (0 a 30): "))
    bonos = float(input("Ingrese los bonos: "))
    otras_deducciones = float(input("Ingrese las otras deducciones: "))

    salario_proporcional = (salario_mensual * dias_trabajados) / 30
    devengado = salario_proporcional + bonos
    neto = (devengado * 0.83) - otras_deducciones
    
    print("Neto:",round (neto, 2))
    
    contador_trabajadores = contador_trabajadores + 1
    
    salario_mensual = float(input("Ingrese el siguiente salario mensual (0 para terminar): "))

if contador_trabajadores == 0:
    print("Sin trabajadores")
