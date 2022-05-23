def tenure_range(year):
    if year < 2:
        return 'less than two'
    elif year < 5:
        return 'between two and five'
    else:
        return 'more than five'

def groupByBucket(salaries_and_tenures:list):
    bucketList={'less than two':[], 'between two and five':[],'more than five':[]}
    for i,j in salaries_and_tenures:
        bucketList[tenure_range(j)].append(i)
    bucketDict={tenure:sum(salaries)/len(salaries) for tenure, salaries in bucketList.items()}
    return bucketDict

salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7),
(76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]



salaries_and_tenures.sort(key=lambda x:x[1])
print(salaries_and_tenures)

print(groupByBucket(salaries_and_tenures))