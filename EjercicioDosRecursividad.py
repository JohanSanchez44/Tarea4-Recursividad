# * Tarea 4 * #

# Contar los digitos de un entero positivo

def conteoDigitos(entero):
    
    if entero == 0:
        return 0
    
    return conteoDigitos(entero // 10) + 1

k = 7
rest = conteoDigitos(k)
print("La cantidad de digitos es: ", rest)