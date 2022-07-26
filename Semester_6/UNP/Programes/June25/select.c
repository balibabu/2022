/*Select program to Watch stdin (fd 0) to see when it has input*/

#include<sys/select.h>
#include<sys/time.h>
#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>


int main(void){
int retval;
fd_set rfds;
struct timeval tv;

FD_ZERO(&rfds);
FD_SET(0, &rfds);

tv.tv_sec = 5;
tv.tv_usec =0;


//int select(nfds, fd_set *readfds, fd_set *writefds, fd_set *exceptfds, struct timeval *timeout);
retval = select(1, &rfds, NULL, NULL, &tv);


if (retval == -1)
 {
        perror("select()");
        }
    else if (retval){
        printf("Data is available now.\n");
         if(FD_ISSET(0, &rfds))
         printf("FD_0 is set");
        }
    else
    {
        printf("No data within five seconds.\n");
        }
    return 0;
}
