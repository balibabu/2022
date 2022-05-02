def split(arr):
    if len(arr)==2:
        merge(arr[:1],arr[1:])
        
def merge(arr1,arr2):
    print(arr1,arr2)
    
split([1,2])