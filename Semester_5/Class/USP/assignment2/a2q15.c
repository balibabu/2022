#include <stdio.h>
void sum_n_avg(double n1,double n2,double n3,double *sump,double *avgp){
    *sump=n1+n2+n3;
    *avgp=*sump/3;
}
int main(){
        double n1,n2,n3,sump, avgp;
        printf("enter three no.\n");
        scanf("%lf%lf%lf", &n1,&n2,&n3);
        sum_n_avg(n1,n2,n3,&sump,&avgp);
        printf("sum=%lf\n",sump);
        printf("average=%lf\n",avgp);
        return 0;
} 
