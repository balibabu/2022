print('question-1')

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for i in range(0, 10):
    if (c[i]%2 == 0):        #gives sum of even numbers
        result += c[i]
print(result)


print('\n\n\nquestion-2')

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for i in range(0, 10):
    if (c[i]%2 != 0):       #gives sum of odd numbers
        result += c[i]
print(result)


print('\n\n\nquestion-3')

subject = 'computer'
subject = list(subject)
ch = subject[0]
for i in range(0, len(subject)-1):
    subject[i] = subject[i+1]
subject[len(subject)-1]=ch
print(''.join(subject))         #omputerc  {single.join(discrete)}

print('\n\n\nquestion-4')

quantity = [15, 30, 12, 34, 56, 99]
total = 0
for i in range(0, len(quantity)):
    if (quantity[i] > 15):      # sum of quantity greater than 15
        total += quantity[i]
print(total)            #219

print('\n\n\nquestion-5')

x = [1, 2, 4, 6, 9, 10, 14, 15, 17]
for i in range(0, len(x)):
    if (x[i]%2 == 0):
        x[i] = 4*i
    elif (x[i]%3 == 0):
        x[i] = 9*i
    else:
        x[i] *= 2
print(x)