from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2017, 2018]
plt.bar(mentions,years)
plt.xlabel("mentions")
plt.ylabel("years")
plt.title("Barplot: mentions vs years")
#plt.show()

plt.axis([499,506,0,2250])
plt.show()

