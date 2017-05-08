def dividir(n,m):
    if (n >= m):
        return dividir(n-m,m) + 1
    return 0

print(dividir(40,5))
