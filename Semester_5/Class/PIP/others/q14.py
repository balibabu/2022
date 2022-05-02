import sys
m=int(sys.argv[1])
d=int(sys.argv[2])
print((3<m<6) or (m==3 and d>20) or (m==6 and d<20) and (d<=31))

'''
if(3<m<6):
    print(True)
elif (m==3 and d>20):
    print(True)
elif (m==6 and d<20):
    print(True)
else:
    print(False)
'''
