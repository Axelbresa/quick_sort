# Funcion quick_Sort que ordena la lista pasando un array como parametro
def quick_sort(arr):
    # Si los elementos de la lista son menor o igual 1 entonces devuelve el array y no realiza ninguna operacion
    if len(arr)<=1:
        return arr

    izquierda=[]
    derecha=[]
    pivote=arr[0]

    # Recorre la lista y decimos que empieze de la posicion 1
    for i in range(1, len(arr)):
    #Si es menor a pivote entonces se guarda en el array izquierda
        if pivote>arr[i]:
            izquierda.append(arr[i])
    #Si es mayor a pivote entonces se guarda en el array derecho
        elif pivote<arr[i]:
            derecha.append(arr[i])
    # Concatena izquierda, pivote y derecha y lo devuelve en un array 
    return quick_sort(izquierda) + [pivote] + quick_sort(derecha)

# Comprobaciones de las lista
print(quick_sort([]))
print(quick_sort([10]))
print(quick_sort([2,4,1,10]))
print(quick_sort([3,1,7,4,5,0,2,-232, 234,100, -100, 1000, -3000,-2,9,8, 52, -76, 10000]))



