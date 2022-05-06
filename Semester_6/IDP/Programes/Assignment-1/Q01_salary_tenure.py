def tenure_range(year):
    if year < 2:
        return 'less than two'
    elif year < 5:
        return 'between two and five'
    else:
        return 'more than five'


salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7),
(76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]

sum_of_salaries=0
for x,y in salaries_and_tenures:
    sum_of_salaries+=x
    print(tenure_range(y))


print('\naverage salaries is',sum_of_salaries/len(salaries_and_tenures))

salaries_and_tenures.sort(key=lambda x:x[1])
print(salaries_and_tenures)