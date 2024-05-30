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
    return quick_sort(izquierda) + [pivote] + quick_sort(derecha)

print(quick_sort([3,1,7,4,5,0,2,-232, 234,100, -100, 1000, -3000,-2,9,8, 52, -76, 10000]))


