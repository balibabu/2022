# Write  a python program that prompts the user to enter a weight in pounds and height in inches anddisplays the BMI
pound=float(input('enter your body weight in pound '))
height=float(input('enter your height in inches '))
bmi= (0.45359237*pound)/((0.0254*height)**2)
print('BMI is %0.4f'%bmi)
