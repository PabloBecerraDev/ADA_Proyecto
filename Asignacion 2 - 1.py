#primera opcion, no se si este correcta, el algoritmo no funciona

def buscar_indice_valor(vector, inicio, fin):
    if inicio > fin:
        return False
    
    medio = (inicio + fin) // 2
    
    if vector[medio] == medio:
        return True
    elif vector[medio] > medio:
        return buscar_indice_valor(vector, medio + 1, fin)
    else:
        return buscar_indice_valor(vector, inicio, medio - 1)



vector = [5, 4, 3, 2, 1, 0]
resultado = buscar_indice_valor(vector, 0, len(vector) - 1)
#print(resultado)

#segunda opcion, el algoritmo funciona pero no es recursivo
def coincide_con_indice(vector):
    for i in range(len(vector)):
        if vector[i] == i:
            return True
    return False

#print(coincide_con_indice(vector))

# el algoritmo funciona y si es recursivo
def buscar(vector, indice):
    if not vector or indice > len(vector) - 1:
        return False
    
    if vector[indice] == indice:
        return True
    else:
        return buscar(vector, indice + 1)
    
print(buscar(vector, 0))
    
    