def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i,len(arr)):
            if arr[min]>arr[j]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]

arr=['balloon','apple','dog','card']
print(arr)
selectionSort(arr)
print(arr)


