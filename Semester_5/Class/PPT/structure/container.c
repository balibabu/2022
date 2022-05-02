#include <stdio.h>
// this is container structure
struct date{
        int dd;
        int mm;
        int yy;
};
struct student{ 
    int regd;
    char nm[20];
    struct date dob;
};
int main(){
    
    return 0;
} 