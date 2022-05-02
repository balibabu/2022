greeting = 'Good Morning. Have a Good Day!!'
print(greeting.count('Good'))
print(greeting.find('a'))
print(greeting.rfind('a'))
print(greeting.capitalize())  #capitalize help: makes 1st letter capital and remaining small
print(greeting.lower())
print(greeting.upper())
print(greeting.swapcase())
print(greeting.istitle())
print(greeting.replace('Good', 'Sweet'))
print(greeting.strip())
print(greeting.split())     #split help: default value of split is space and also gives empty string eg:''
print(greeting.partition('.')) #partition help: same like split but it includes the delimeter
print(greeting.startswith('good')) #startswith help: it is case sensitive
print(greeting.endswith('!!'))