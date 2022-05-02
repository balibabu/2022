class Set:

    def __init__(self,arr):
        self.arr=arr

    def getSubsets(self):
        def subset(arr, l, r, sum1=[]):
            if l > r:
                print(sum1)
                return
            sum1.append(arr[l])
            subset(arr, l + 1, r, sum1)
            sum1.pop()
            subset(arr, l + 1, r, sum1)
        subset(self.arr,0,len(self.arr)-1)


arr=eval(input('enter a list:'))
s1=Set(arr)
temp=s1.getSubsets()