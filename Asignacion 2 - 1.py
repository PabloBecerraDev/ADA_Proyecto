

vector = [5, 4, 3, 2, 1, 0]

# el algoritmo funciona y si es recursivo
def buscar(vector, indice):
    if not vector or indice > len(vector) - 1:
        return False    
    if vector[indice] == indice:
        return True
    else:
        return buscar(vector, indice + 1)
    
print(buscar(vector, 0))
    
    