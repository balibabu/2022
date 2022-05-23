import math
from matplotlib import pyplot as plt

x_values=[i for i in range(-10,11)]
xsinx=[(x*math.sin(x)) for x in x_values]
x2sinx=[(pow(x,2)*math.sin(x)) for x in x_values]
x3sinx=[(pow(x,3)*math.sin(x)) for x in x_values]
x4sinx=[(pow(x,4)*math.sin(x)) for x in x_values]

plt.plot(x_values,xsinx,label='xsinx',color='red',linestyle='solid')
plt.plot(x_values,x2sinx,label='x2sinx',color='GREEN',linestyle='solid')
plt.plot(x_values,x3sinx,label='x3sinx',color='blue',linestyle='solid')
plt.plot(x_values,x4sinx,label='x4sinx',color='black',linestyle='solid')

plt.legend(loc=9)
plt.show()