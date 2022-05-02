def isPalindrome(num):
    temp = num
    rev = 0
    while (temp > 0):
        rev = rev * 10 + temp % 10
        temp //= 10
    return num == rev


num = int(input('enter a number '))
print("Is it palindrome?", isPalindrome(num))

