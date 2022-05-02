'''5. Write a recursive function to calculate the geometric sum of first n terms with constant ration r, where r lies in the interval (0,1). Note: In mathematics, a geometric
series is a series with a constant ratio between successive terms. For example, if n =
4 and r = (1/2) then output should be (1+1/2+1/4+ 1/8 ) = 1.875'''
def geometric(terms,ratio):
    if terms==1 or terms==0:
        return terms
    return ratio**(terms-1)+geometric(terms-1,ratio)

t=int(input('enter no. of terms:'))
r=float(input('enter ratio:'))
print(geometric(t,r))