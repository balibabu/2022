'''H2.Q13. Enter the basic salary of an employee of an organization through the command prompt. His 
dearness allowance (DA) is 40% of basic salary, and house rent allowance (HRA) is 20% 
of basic salary. Write a python program to calculate his gross salary.'''
import sys
bSalary=float(sys.argv[1])
DA=0.4*bSalary
HRA=0.2*bSalary
gross_salary=bSalary+DA+HRA
print("your gross salary is ",gross_salary)
