def hanoi(n,source,spare,target):
    if n==0:
        print('there is no disk to move')
    elif n==1:
        print('move a disk from',source,'to', target)
    else:
        hanoi(n-1,source,target,spare)
        print('move a disk from',source,'to',target)
        hanoi(n-1,spare,source,target)

disks=int(input('enter no.of disk '))
hanoi(disks,'A','B','C')
