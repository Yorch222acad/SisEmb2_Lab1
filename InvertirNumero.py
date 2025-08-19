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


print("Ingrese cuantos números ingresará")
CantidadNum = int(input())
LNum = Ingresar_numeros(CantidadNum)
print("Los números son:", LNum)


print("Ingresa un número a invertir")
numToInv = int(input())
numInv = Invertir_numero(numToInv)
print("El número invertido es:", numInv)