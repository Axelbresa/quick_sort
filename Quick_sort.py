lista=[3,1,7,4,5,0,2,-2,9,8]

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    izquierda=[]
    derecha=[]
    pivote=arr[0]

    for i in range(1, len(arr)):
        if pivote>arr[i]:
            izquierda.append(arr[i])
        elif pivote<arr[i]:
            derecha.append(arr[i])
    return izquierda, pivote, derecha

def repit_funcion(lista):
    if len(lista)<2:
        return lista
    
    izquierda, pivote, derecha=quick_sort(lista)
    iz=quick_sort(izquierda) 
    de=quick_sort(derecha) 
    result=iz+ pivote +de

    return result
    # + quick_sort(derecha)

print(repit_funcion(lista))
