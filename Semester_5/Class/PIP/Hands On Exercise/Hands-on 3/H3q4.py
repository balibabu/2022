'''You can use Cramer’s rule to solve the following 2 X 2 system of linear equation:
Write a python program that prompts the user to enter a, b, c, d, e, and f and displays the
result. If ad - bc is 0, report that “The equation has no solution.”'''
def cramer_rule(a,b,c,d,e,f):
    denominator=a*d-b*c;
    if denominator==0:
        print('The equation has no solution')
    else:
        x=(e*d-b*f)/denominator
        y=(a*f-e*c)/denominator
        print('x is',x,'y is',y)



print('linear equations:\nax+by=e\ncx+dy=f')
print('enter value of a,b,c,d,e and f')
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
cramer_rule(a,b,c,d,e,f)