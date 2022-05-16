import matplotlib.pyplot as plt

# Unequal axis
test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]
plt.scatter(test_1_grades,test_2_grades)
plt.axis([70, 105, 50, 105])
plt.show()

# Equal axis
test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]
plt.scatter(test_1_grades,test_2_grades)
plt.axis([50, 105, 50, 105]) #[x-min,x-max, y-min,y-max]
plt.show()