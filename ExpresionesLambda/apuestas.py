# Ejercicio de apuestas para encontrar el que mas gano y el que mas perdio

from functools import reduce

items = [[[1, 2, 3], [0, 1, 1]], [[100, 20, 30], [0, 1, 0]], [[1, 2, 3], [1, 1, 1]]]

def group(lista, listb):
    return list(map(lambda x, y: (x, y), lista, listb))

def composed_group(mother_of_lists):
    return list(map(lambda x: group(x[0], x[1]), mother_of_lists))

def minify(item):
    return list(map(lambda x: x[0] if x[1] else -x[0], item))

def composed_minify(mother_of_lists):
    return list(map(lambda x: minify(x), mother_of_lists))

def operate(arr):
    return reduce(lambda x, y: x + y, arr)

def composed_operate(mother_of_lists):
    return list(map(lambda x: operate(x), mother_of_lists))


grouped = group(items[0][0], items[0][1])
minified = minify(grouped)
result = operate(minified)

print(minified)
print(result)


jeje = composed_group(items)
jaja = composed_minify(jeje)
jiji = composed_operate(jaja)
print(jeje)
print(jaja)
print(jiji)
