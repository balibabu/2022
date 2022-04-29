def getHeader():
    return '<?xml version="1.0" encoding="UTF-8" standalone="no"?><!--Created with JFLAP 7.1.--><structure>&#13;\n	<type>fa</type>&#13;\n	<automaton>&#13;\n'

def getFooter():
    return '\n	</automaton>&#13;\n</structure>'    

def getState():
    id=int(input('enter an id eg:0,1,..: '))
    stateName=input('enter state name eg: q0,q1,..: ')
    isInitial=input('is it initial state: 0 or 1: ')
    if isInitial == '':
        isInitial=0
    isFinal=input('is it final state: 0 or 1: ')
    if isFinal == '':
        isFinal=0
    x=id*100+100
    y=150
    string=f'\n<state id="{id}" name="{stateName}">&#13;<x>{x}</x>&#13;<y>{y}</y>&#13;{"<initial/>&#13;"*int(isInitial)}{"<final/>&#13;"*int(isFinal)}</state>&#13;\n'
    return string

def getTransition():
    _from=input('from stateID: ')
    _to=input('to stateID: ')
    values=input('enter transactions with spaces: ').split(' ')
    query='\n'
    for i in values:
        query+=f'<transition>&#13;<from>{_from}</from>&#13;<to>{_to}</to>&#13;<read>{i}</read>&#13;</transition>&#13;\n'
    return query

def main():
    f1=open(input('enter file name: ')+'.jff',"w")
    f1.write(getHeader())
    print('Menu\n1. Add state\n2. Add transaction\n3. Done\n')
    while(1):
        print('\nEnter your choice from Menu: ')
        choice=int(input())
        if(choice==1):
            f1.write(getState())
        elif(choice==2):
            f1.write(getTransition())
        elif(choice==3):
            break
        else:
            print('invalid option')

    f1.write(getFooter())
    f1.close()
    print('done')

main()