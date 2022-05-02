#include <stdio.h>
void sub(float *valp,char *letp,int *countp){
    printf("x=%f\n",*valp);
    printf("code=%c\n",*letp);
    printf("many=%d\n",*countp);
    
    
}
int main()
{
        float x=17.1;
        char code='g';
        int many=14;
        sub(&x,&code,&many);

        return 0;
} 