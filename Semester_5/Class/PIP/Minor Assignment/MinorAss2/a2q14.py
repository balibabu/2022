'''14. Write a function named as ‘UpperCase’ which converts the lower case alphabet to uppercase alphabet.
Also, assert that the entered alphabet by user is valid lowercase alphabet. Write a function main that
accepts inputs from the user interactively and converts the lowercase alphabet to uppercase using the
function ‘UpperCase’.'''

def UpperCase(ch):
    asciich=ord(ch)
    assert 97<=asciich<=122, "Do not enter Uppercase"
    return chr(asciich-32)

def main():
    ch=input('enter an alphabet ')
    print('Uppercase of',ch,'is',UpperCase(ch))

main()
