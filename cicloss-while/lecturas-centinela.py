
suma = 0
intento = 1

while True:
    num = int(input("Digite un numero: "))
    if num != -50 or intento != 1:
        suma += num
    else:
        break

print("Suma: ", suma)