'''from integer to roman'''

symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values =  [1,    5,  10,  50,  100,  500, 1000]

def getRoman(num,pos=len(values)-1):
    if num == 0:
        return ''
    elif num >= values[pos]:
        return symbols[pos]+getRoman(num-values[pos],pos)
    elif (num >= (values[pos]-values[pos-2])) and pos%2==0:
        return symbols[pos-2]+symbols[pos] + getRoman(num - (values[pos]-values[pos-2]), pos-2)
    elif (num >= (values[pos]-values[pos-1])) and pos%2==1:
        return symbols[pos-1]+symbols[pos] + getRoman(num - (values[pos]-values[pos-1]), pos-1)
    else:
        return getRoman(num, pos-1)



print(getRoman(int(input('enter a number:'))))

