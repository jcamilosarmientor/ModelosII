#Obtener el valo absoluto de un número
def absoluto(n):
    if n >= 0:
        return n
    else:
        return producto(n*-1)

print (absoluto(-5))
