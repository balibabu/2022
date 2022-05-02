def rev(str):
    if len(str)==1:
        return str
    else:
        return rev(str[1:])+str[0]

print(rev('apple'))
