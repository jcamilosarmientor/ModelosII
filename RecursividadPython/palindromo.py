def palindromo(texto, inicio, fin):
    if inicio == fin:
        return True
    if texto[inicio] == texto[fin]:
        return palindromo(texto, inicio + 1, fin - 1)
    else:
        return False

print(palindromo('bob', 0, len('bob') - 1))
