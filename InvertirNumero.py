def invertir_numero(n):
    inv = 0
    while n>0:
        dg = n%10
        inv = inv*10+dg
        n//=10
    return inv

print("Ingresa un número a invertir")
numToInv = int(input())
numInv = invertir_numero(numToInv)
print("El número invertido es:", numInv)