'''The self.symbols are I, V, X, L, C, D, and M, standing respectively for 1, 5, 10, 50, 100, 500,
and 1,000 in the Hindu-Arabic numeral system. A symbol placed after another of equal or
greater value adds its value; e.g., II = 2 and LX = 60.'''
#roman to integer
class Roman1:
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values =   [1,   5,   10, 50,  100, 500, 1000]
    def __init__(self,num):
        self.num=num
    def getRoman(self):
        temp=self.num
        rom=''
        pos,c=0,0
        digit=1
        while temp:
            digit=(temp%10)*10**(c)
            temp//=10

            if(digit<=self.values[pos]*3):
                rom=self.symbols[pos]*(digit//(10**(c)))+rom
            elif digit==self.values[pos+1]-self.values[pos]:
                rom = self.symbols[pos]+self.symbols[pos+1] + rom
            elif digit==self.values[pos+2]-self.values[pos]:
                rom = self.symbols[pos]+self.symbols[pos+2] + rom
            else:
                rom = self.symbols[pos+1]+self.symbols[pos]*((digit-self.values[pos+1])//(10**(c)))  + rom
            pos+=2
            c+=1
        return rom

r=Roman1(int(input('enter a number: ')))
print(r.getRoman())