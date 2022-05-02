def bubbleSort(arr):
    for i in range(len(arr)-1):
        swap=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                swap=True
                arr[j] , arr[j + 1]=arr[j+1],arr[j]
                print('arranging...')
        if not swap: return

# a=['egg','cat','dog','apple','ball','cat']
a=['apple', 'ball', 'cat', 'cat', 'dog', 'egg']
bubbleSort(a)
print(a)