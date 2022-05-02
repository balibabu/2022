#include <stdio.h>
struct student{
    int roll[3];
    double x;
}s1;
int main()
{
    printf("%lu\n",sizeof(s1.roll));
    printf("%lu\n",sizeof(s1.x));
    printf("%lu\n",sizeof(s1));
    return 0;
} 