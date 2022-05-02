#integer to roman
class Roman2:
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = [1, 5, 10, 50, 100, 500, 1000]
    def __init__(self,str1):
        self.rom=str1

    def getInteger(self):
        queue=list(self.rom)
        self.num=0
        while(queue!=[]):
            a=queue.pop(0).upper()
            if(queue==[]):
                return self.values[(self.symbols.index(a))]
            b=queue[0].upper()
            if a==b:
                queue.pop(0)
                self.num += self.values[self.symbols.index(a)]
                self.num += self.values[self.symbols.index(b)]
                if(queue!=[] and queue[0]==b):
                    self.num += self.values[self.symbols.index(queue.pop(0))]
            elif self.symbols.index(a)<self.symbols.index(b):
                queue.pop(0)
                self.num+=self.values[self.symbols.index(b)]- self.values[self.symbols.index(a)]
            else:
                self.num += self.values[self.symbols.index(a)]
        return self.num

r=Roman2(input('enter a roman number: '))
print(r.getInteger())

