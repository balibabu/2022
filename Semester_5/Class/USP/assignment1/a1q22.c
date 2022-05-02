#include <stdio.h>

int main()
{
    int a=0,b=0,c=0,f=0,mark,total=0,nof=0;
    printf("to stop entering marks enter -1\n");
    printf("enter your marks\n");
    do
    {
        scanf("%d",&mark);
        if (mark>=0){
            if (mark>=80)
                a++;
            else if(mark>=65)
                b++;
            else if(mark>=40)
                c++;
            else
                f++;
            total+=mark;
            nof++;
        }else
            printf("Invalid mark\n");

    } while (mark!=-1);

    printf("No. of students with Grade A is %d\n",a);
    printf("No. of students with Grade B is %d\n",b);
    printf("No. of students with Grade C is %d\n",c);
    printf("No. of students with Grade F is %d\n",f);
    printf("Average is %.2lf\n",(1.0*total/nof));
    
    
    return 0;
} 