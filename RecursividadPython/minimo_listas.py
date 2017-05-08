def minimo(lista):
  """Obtener el menor elemento de una lista"""
	if len(lista) == 1:
		return lista[0]
	
	if lista[0] < lista[1]:
		return minimo([lista[0]]+lista[2:])
	else:
		return minimo(lista[1:])

def minimo_listas(listas):
  """Retornar una lista de todos los valores minimos"""
	if len(listas) == 0:
		return []
	
	else:
		return [minimo(listas[0])] + sol(listas[1:])
    
    
    

print(minimo_listas([[1,4,5,2],[9,10,3,1],[7,7,2,3]]))
