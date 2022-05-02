address = 'B-6, Lodhi road, Delhi'
print(len(address))
print(address[17:-1])
print(address[-len(address): len(address)])
print(address[:-12] + address[-12:])
print(address.find('delhi'))    #find help:(it's case sensitive) returns -1 if not present otherwise first index
print(address.swapcase())
print(address.split(','))  #return list
print(address.isalpha())