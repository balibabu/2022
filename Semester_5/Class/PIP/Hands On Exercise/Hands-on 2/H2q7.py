eggs=int(input("enter your no. of eggs "))
gross=eggs//144
eggs=eggs%144
dozen=eggs//12
eggs=eggs%12
print('Your number of eggs is ',gross,' gross ',dozen,' dozens ',eggs)
