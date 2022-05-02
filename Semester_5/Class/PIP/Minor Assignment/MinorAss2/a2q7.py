'''Write a function areaTriangle that takes the lengths of three sides: side1, side2, and side3 of the
triangle as the input parameters and returns the area of the triangle as the output. Also, assert that sum
of the length of any two sides is greater than the third side. Write a function main that accepts inputs
from the user interactively and computes the area of the triangle using the function areaTriangle.'''
def areaTriangle(side1,side2,side3):
	s=(side1+side2+side3)/2
	print(type(s))
	area=pow(s*(s-side1)*(s-side2)*(s-side3),0.5)
	return area

side1=int(input("enter 1st side of triangle "))
side2=int(input("enter 2nd side of triangle "))
side3=int(input("enter 3rd side of triangle "))

assert ((side1+side2)>side3 and (side1+side3)>side2 and (side2+side3)>side1),"sum of the length of any two sides of triangle is greater than the third side"
print("area of triangle is",areaTriangle(side1,side2,side3))
