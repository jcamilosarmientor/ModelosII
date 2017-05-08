def conversorBinario(n, binario = []):
    if (n >= 1):
            binario[len(binario):] = [n%2]
            return conversorBinario(n/2)
    else :
        return binario

def binadec(n):
    if n < 10:
        return n
    else :
        return (n%2) + binadec(n/10) * 2

print (binadec(111))
#print (conversorBinario(357).reverse())
