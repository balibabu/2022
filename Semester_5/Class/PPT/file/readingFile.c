#include <stdio.h>
int main(){
    FILE *fp;
    char fname[31];
    int nol=1,now=0,noc=0;
    char ch;
    printf("enter file name ");
    scanf("%s", fname);
    
    fp=fopen(fname,"r");
    if (fp==NULL)
    {
        printf("err openinf file");
        return 1;
    }
    
    while(1){
        ch=fgetc(fp);
        if (ch==EOF)
            break;
        noc++;
        if(ch==' ' || ch=='\t'){
            noc--;
            now++;
        }        
        if (ch=='\n')
        {
            noc--;
            now++;
            nol++;
        }
    }
    printf("nol=%d  now=%d  noc=%d\n",nol,now,noc);
    fclose(fp);
    return 0;
} 