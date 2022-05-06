import math
from matplotlib import pyplot as plt

x_values=[i for i in range(-10,11)]
xsinx=[(x*math.sin(x)) for x in x_values]
x2sinx=[(x*x*math.sin(x)) for x in x_values]
plt.plot(x,xsinx,color='red',linestyle='solid')
plt.plot(x,x2sinx,color='red',linestyle='solid')

plt.show()