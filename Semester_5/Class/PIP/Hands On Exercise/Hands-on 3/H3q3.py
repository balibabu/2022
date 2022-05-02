'''The two roots of a quadratic equation 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0 can be obtained using the
following formula:
𝑟1 = −𝑏+√2𝑏𝑎2−4𝑎𝑐
 and 𝑟2 = −𝑏−√2𝑏𝑎2−4𝑎𝑐
b2 - 4ac is called the discriminant of the quadratic equation. If it is positive, the equation has
two real roots. If it is zero, the equation has one root. If it is negative, the equation has no real
roots.
Write a python program that prompts the user to enter values for a, b, and c and displays the
result based on the discriminant. If the discriminant is positive, display two roots. If the
discriminant is 0, display one root. Otherwise, display “The equation has no real roots”'''

def roots_quadrtic(a,b,c):
    discriminant=b*b-4*a*c
    if discriminant<0:
        print('The equation has no real roots')
    elif discriminant==0:
        r1 = (-b + pow(discriminant, 0.5)) / (2 * a)
        print('the root is',r1)
    else:
        r1 = (-b + pow(discriminant, 0.5)) / (2 * a)
        r2 = (-b - pow(discriminant, 0.5)) / (2 * a)
        print('the roots are',r1,'and',r2);

print('enter value of a,b and c')
a=float(input())
b=float(input())
c=float(input())
roots_quadrtic(a,b,c)