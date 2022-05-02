def custom_sort(str1):
    arr=str1.split('-')
    arr.sort()
    str2 = arr[0]
    for i in range(1,len(arr)):
        str2+='-'+arr[i]
    return str2

str1=input('enter a string:')
print(str1)
print(custom_sort(str1))