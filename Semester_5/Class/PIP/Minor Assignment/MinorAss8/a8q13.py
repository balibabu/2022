'''13. Write a recursive function that inserts the element x at every kth position in the given
list, and returns the modified list. For example, if we wish to insert element 50 at
every 3rd position (counting 0, 1, 2, 3) in the list [1, 2, 3, 4, 5, 6, 7], the output list
will be [1, 2, 3, 50, 4, 5, 6, 50, 7]. ’'''
def fun(lst,element,position):
    if len(lst)<position:
        return lst
    temp=lst[:position]
    temp.append(element)
    return temp+fun(lst[position:],element,position)

lst=eval(input('enter a list\n'))
element=int(input('enter an element:'))
position=int(input('enter position:'))
print(fun(lst,element,position))