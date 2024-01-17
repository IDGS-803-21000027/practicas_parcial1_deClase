num1= int(input("Dame la cantidad de asteriscos para la base \n"))

for i in range(num1):
    print("*"*(i+1))


cantidad = int(input("Cuantos numeros quieres leer \n"))
numeros = []
for i in range(cantidad):
    numeros.append(int(input("Ingresa el numero \n")))

numeros.sort()

miDic = {}

print("-------PARES E IMPARES-------")
for i in numeros:
    miDic[i] = miDic.get(i, 0) + 1

    if i % 2 == 0:
        print("el numero: " + str(i) + " es par")
    else: print("el numero: " + str(i) + " es impar")

print("-------VECES DE APARICION-------")
for i, c in miDic.items():
    print("El numero: " + str(i) + " aperecio: " + str(c) + " veces")

