def mul(a,b):
	print(__name__)
	print('product is',a*b)

#if __name__=='__main__':
	#mul(5,2)


class A:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def print(self):
		print("X is:",self.x,"Y is:",self.y)
		

x = A(5,4)
x.print()
