from matplotlib import pyplot as plt
def sumOfDigit(num):
    sum_digits=0
    while(num):
        sum_digits+=num%10
        num//=10
    return sum_digits

lowerR=int(input('enter lower range '))
upperR=int(input('enter upper range '))

perfectSq=[]
numList=[]
for i in range(lowerR,upperR+1):
    a=pow(i,2)
    if a <= upperR and sumOfDigit(a)<10:
        perfectSq.append(a)
        numList.append(i)


plt.plot(perfectSq,numList,color='red')
plt.title('Perfect Squares')
plt.xlabel('squares --------->')
plt.ylabel('numbers ---------->')
plt.show()