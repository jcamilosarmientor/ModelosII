def sumatoria(n):
    if n/100 > 0:
        return (n/100) + sumatoria(n - ((n/100)*100))
    elif n/10 > 0:
        return (n/10) + sumatoria(n - ((n/10)*10))
    elif n < 10:
        return n

print (sumatoria(351))
