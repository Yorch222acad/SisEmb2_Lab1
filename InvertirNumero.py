def Invertir_numero(n):
    inv = 0
    while n>0:
        dg = n%10
        inv = inv*10+dg
        n//=10
    return inv
def Ingresar_numeros(n):
    aux = 1
    l = []
    while aux!=(n+1):
        print("Ingrese el número:", aux)
        aux2 = int(input())
        l.append(aux2)
        aux += 1
    return l
def Ingresar_nombre():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    profesion = input("Ingrese su profesión: ")

    print(f"Hola {nombre}, tienes {edad} años y eres {profesion}. ¡Mucho gusto!")
    return 0
def Numeros_unicos():

    x = int(input("¿Cuántos números vas a ingresar?: "))
    numeros = []

    for i in range(x):
        num = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)

    unicos = list(set(numeros))  # elimina duplicados
    print(f"Los valores únicos son: {unicos}")

print("Ingrese cuantos números ingresará")
CantidadNum = int(input())
LNum = Ingresar_numeros(CantidadNum)
print("Los números son:", LNum)


print("Ingresa un número a invertir")
numToInv = int(input())
numInv = Invertir_numero(numToInv)
print("El número invertido es:", numInv)

x=Ingresar_nombre()
y=Numeros_unicos()
