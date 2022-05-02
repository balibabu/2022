minutes=int(input('enter the number of minutes '))
days=minutes//1440
year=days//365
days%=365
print(minutes,' minutes is approximately ',year,' year and ',days,' days')
