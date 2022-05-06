from matplotlib import pyplot as plt

maxT= [17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
minT= [-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]
months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
plt.plot(months,maxT,color='red',marker='o',linestyle='solid')
plt.plot(months,minT,color='blue',marker='o',linestyle='solid')
plt.xticks(rotation=45)
plt.show()