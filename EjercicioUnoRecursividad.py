# * Tarea 4 * #

# Crear una lista de enteros en Python y realizar la suma con recursividad, el caso
# base es cuando la lista esta vacia. 

def suma(n, lista):
    if n == 0:
        return 0
    if n == 1:
        return lista[0]
    
    return lista[n - 1] + suma(n - 1, lista)

nums = []
n = len(nums)
print("La suma tiene como resultado: ", suma(n, nums))

