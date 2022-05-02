'''ends with return bool'''
print('bali'.endswith('i'))
print('bali'.startswith('i'))

'''encoding'''
msg='hello gita'
print(msg)
msg=msg.encode('utf-32')
print(msg)
msg=msg.decode('utf-32')
print(msg)
print(msg.encode('utf-8'))
print('===================================================\n\n')

'''join: joins the array of strings'''
strTup=('bali','babu','hello')
x='chauhan'.join(strTup)
print(x)

print('12345'.join('abcde'))
print('12345'.join('a'))
strTup=('bali','babu','chauhan')

print(''.join(strTup))

input()

