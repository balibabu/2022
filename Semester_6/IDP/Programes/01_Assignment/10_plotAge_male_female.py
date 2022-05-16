import matplotlib.pyplot as plt

# Male
male_age = [53,51,71,31,33,39,52,27,54,30,64,26,21,54,52,20,59,32]
histogram1=Counter(x//5*5 for x in male_age)
plt.bar(
    histogram1.keys(),
    histogram1.values(),
    width=5,
    edgecolor=(0,0,0)
)
plt.xticks([x*5 for x in range(3,16)])
plt.title("Histogram for age of male")
plt.ylabel("number of male")
plt.xlabel("age of male")
plt.show()


# Female
female_age = [53,65,68,21,75,46,24,63,61,24,49,41,39,40,25,54,42,32,48,23,23]
histogram2=Counter(x//5*5 for x in female_age)
plt.bar(
    histogram2.keys(),
    histogram2.values(),
    width=5,
    edgecolor=(0,0,0)
)
plt.xticks([x*5 for x in range(3,16)])
plt.title("Histogram for age of female")
plt.ylabel("number of female")
plt.xlabel("age of female")
plt.show()