def invertir(lista):
	if len(lista) == 1:
		return lista
	return [lista[-1]] + invertir(lista[:-1])

