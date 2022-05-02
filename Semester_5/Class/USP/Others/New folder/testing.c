#include <stdio.h>

int main()
{

    int fd1 = open("fool1.txt", O_RDONLY | O_CREAT); 
    close(fd1);
    int fd1 = open(".\fool2.txt", O_RDONLY | O_CREAT); 

    return 0;
}