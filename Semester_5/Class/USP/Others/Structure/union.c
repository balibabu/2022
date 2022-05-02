#include <stdio.h>
union test{
    int x,y;
    char c[30];
};

int main()
{
    union test s1;
    s1.x = 2;
    printf("\nAfter making x=%d\n",s1.x);
    printf("x=%d\n",s1.x);
    printf("y=%d\n",s1.y);
    printf("c=%s\n\n",s1.c);

    s1.x = 49;
    printf("\nAfter making x=%d\n",s1.x);
    printf("x=%d\n",s1.x);
    printf("y=%d\n",s1.y);
    printf("c=%s\n\n",s1.c);

    union test s2;
    strcpy(s2.c,"bali");
    printf("\nafter naming c=%s\n",s2.c);
    printf("x=%d\n",s2.x);
    printf("y=%d\n\n",s2.y);
    
    printf("size of s1=%lu\n",sizeof(s1));
    printf("size of s2=%lu\n",sizeof(s1));

    return 0;
} 