#include <stdio.h>
//this is nested structure
struct student{ 
    int regd;
    char nm[20];
    struct {
        int dd;
        int mm;
        int yy;
    } dob;
};
int main(){
    
    return 0;
} 