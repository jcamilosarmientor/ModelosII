def suma(lista):
 if lista == []:
	return 0
 else: 
	return lista[0]+suma(lista[1: ])

print(suma([1,2,4,5,6,7]))
