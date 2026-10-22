freno = 99
suma = 0
contador = 0

while True:
    numero = int(input("Ingrese las notas: "))
    if numero != freno:
        suma += numero
        contador += 1
    elif contador == 0:
        print("Cantidad ", contador, "Sin notas: ")
        break    
    else:
        promedio = suma / contador
        print ("Cantidad: ", contador, "Promedio", promedio)
        break

        

    
    