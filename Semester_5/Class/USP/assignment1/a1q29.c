#include <stdio.h>
int isLeapYear(int);
int main()
{
    char month[12][10]={"January","February","March","April","May","June","July","August","September","October","November","December"};
    int days[12]={31,28,31,30,31,30,31,31,30,31,30,31};
    int day,year,total=0,i;
    printf("enter month day and year eg: January 1 1994\n");
    scanf("%s",month);
    scanf("%d%d",&day,&month);
    for (i = 0; i < 12; i++)
    {
        if(month==month[i])
            break;
        total+=days[i];
    }
    total+=day; 
    if (i>2)
        total+=isLeapYear(year);
    return 0;
} 
int isLeapYear(int y){
    if(y%400==0)
        return 1;
    else if(y%4==0 && y%100!=0)
        return 1;
    return 0;
}
/*
jan 31
28
31
30
31
30
31
31
30
31
30
31
*/