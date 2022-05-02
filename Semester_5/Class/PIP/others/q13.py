import sys
income=int(sys.argv[1])
DA=0.4*income
HRA=0.2*income
gross_income=income+DA+HRA
print('Your gross salary is ',gross_income)
