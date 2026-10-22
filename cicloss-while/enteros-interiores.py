a = int(input("Ingrese el entero A: "))

b = int(input("Ingrese el entero B: "))

if a < b-1:
    while a < b-1:
     # orden = list(range(a+1, b))
     a = a + 1
     print("Orden: ", a)
else:
   print("No hay enteros interiores") 
   