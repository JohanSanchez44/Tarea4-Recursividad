# * Tarea 4 * #

# Eliminar de un ADT pila el valor en la posición media.

def eliminarPosMedia(lista, Pos, n, arrAx):
    if n <= 2:
        return print("No existe una posicion media")
        
    if n > Pos:
        num = lista[n - 1]
        arrAx.insert(0, num)
        lista.pop()
    
    elif n == Pos:
        lista.pop()
        lista = lista + arrAx
        return lista
    
    return eliminarPosMedia(lista,Pos , n - 1, arrAx)

arreglo = [1, 2]
n = len(arreglo)
Pos = len(arreglo)//2 + 1
arrAx = []

print(eliminarPosMedia(arreglo, Pos, n, arrAx))
