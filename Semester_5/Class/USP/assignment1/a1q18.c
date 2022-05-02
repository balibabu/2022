#include <stdio.h>

int main()
{
        int n,i;
        char str[30];
        printf("enter a message ");
        scanf("%s",str);
        printf("how many times ");
        scanf("%d",&n);
        for (i = 1; i <= n; i++)
        {
            if(i%10==1)
                printf("%dst %s\n",i,str);
            else if(i%10==2)
                printf("%dnd %s\n",i,str);
            else if(i%10==3)
                printf("%drd %s\n",i,str);
            else
                printf("%dth %s\n",i,str);
        }
        
        return 0;
} 