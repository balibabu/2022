//WAP to implement database operation: insert, delete,, search and list on given record type.
#include <stdio.h>
struct item{
    int itno;
    char name[30];
    float price;
};
int main(){
    struct item s;
    int ch,n,flag=0;
    long int rsize=sizeof(struct item);
    FILE *fp,*tmp;

    fp=fopen("item.dat","r+");
    if(fp==NULL){
        fp=fopen("item.dat","w+");
        if(fp==NULL)
            return 1;
    }

    do{
        printf("\n1.Insert\n2.Search\n3.Update\n4.Remove\n5.List all records\n6.Exit\n");
        scanf("%d", &ch);
        switch(ch){
            case 1:
                fseek(fp,0,SEEK_END);
                printf("Enter item details\n");
                scanf("%d%s%f", &s.itno,s.name,&s.price);
                fwrite(&s,rsize,1,fp);
                break;

            case 2:
                fseek(fp,0,SEEK_SET);
                printf("Enter item number\n");
                scanf("%d", &n);
                while (fread(&s,rsize,1,fp)>0){
                    if(s.itno==n){
                        flag=1;
                        break;
                    }
                }
                if(flag!=0){
                    printf("Record found\n");
                    printf("%d %s %f\n",s.itno,s.name,s.price);
                }else{
                    printf("Record not found\n");
                }
                break;

            case 3:
                fseek(fp,0,SEEK_SET);
                printf("Enter item no.\n");
                scanf("%d", &n);
                while(fread(&s,rsize,1,fp)>0){
                    if(s.itno==n){
                        flag=1;
                        printf("Enter new name and price\n");
                        scanf("%s%f", s.name,&s.price);
                        fseek(fp,-rsize,SEEK_CUR);
                        fwrite(&s,rsize,1,fp);
                        break;
                    }
                }
                if(flag==0)
                    printf("File not found\n");
                break;
            case 4:
                fseek(fp,0,SEEK_SET);
                printf("Enter item no.\n");
                scanf("%d", &n);
                tmp=fopen("temp.dat","w");
                while (fread(&s,rsize,1,fp)>0)
                {
                    if(s.itno!=n)
                        fwrite(&s,rsize,1,tmp);
                }
                fclose(fp);
                fclose(tmp);
                remove("item.dat");
                rename("temp.dat","item.dat");
                fopen("item.dat","r+");
                break;
            case 5:
                fseek(fp,0,SEEK_SET);
                printf("item no.\tName\t\tPrice\n");
                while (fread(&s,rsize,1,fp)>0) 
                {
                    printf("%d\t\t%s\t\t%f\n",s.itno,s.name,s.price);
                }
                break;
            case 6:
                break;
            default:
                printf("Invalid choice\n");
        }
    }while(ch!=6);
    return 0;
} 