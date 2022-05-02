def insertionSort(arr):
    pos=0
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            pos+=1
        else:
            temp=arr[i+1]
            tpos=i
            arr[i + 1]=arr[i]
            while(tpos):
                if(temp>arr[i]): break
                arr[tpos+1]=arr[tpos]
                tpos-=1
            arr[tpos]=temp


a=[1, 6, 5]#4,2,1,3,5]
insertionSort(a)
print(a)