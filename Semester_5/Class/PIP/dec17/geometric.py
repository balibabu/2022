def geometric(ratio,terms):
    if terms==1 or terms==0:
        return terms
    return ratio**(terms-1)+geometric(ratio,terms-1)

print(geometric(2,5))
