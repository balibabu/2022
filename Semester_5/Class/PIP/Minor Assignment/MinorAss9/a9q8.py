'''8. Examine the following function percentage:'''
def percentage(marks, total):
    try:
        percent = (marks / total) * 100
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except:
        print('Any other Error')
    else:
        print(percent)
    finally:
        print('Function percentage completed')

percentage('150.0', '200.0')
'''
(a) percentage(150.0, 200.0) 
75.0
Function percentage completed

(b) percentage(150.0, 0.0)
ZeroDivisionError
Function percentage completed

(c) percentage('150.0', '200.0')
TypeError
Function percentage completed
'''