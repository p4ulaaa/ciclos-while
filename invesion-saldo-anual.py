capital = float(input("Ingrese el capital C: "))
tasa = float(input("Ingrese la tasa anual I: "))
anios = int(input("Ingrese la cantidad de años M: "))

while capital < 0 or tasa <= 0 or tasa >= 100 or anios <= 0:
    print("Datos inválidos. Ingrese la terna nuevamente.")
    capital = float(input("Ingrese el capital C: "))
    tasa = float(input("Ingrese la tasa anual I: "))
    anios = int(input("Ingrese la cantidad de años M: "))

saldo = capital

for i in range(1, anios + 1):
    saldo = saldo * (1 + tasa / 100)
    print("Año", i, ":", saldo)

print("Saldo final:", saldo)