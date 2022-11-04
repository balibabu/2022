#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
int main()
{
    /* code */

    int fd[2];
    int nbytes;
    char charbuffer[100];
    pid_t childpid;

    pipe(fd);

   if((childpid=fork())==-1)
  {
     printf("Error fork()");
     exit(1);

  }  

   else if(childpid==0)

     {
        //
        close(fd[0]);
        write(fd[1], "Hello", 6);

     }
   else
   {
   
   nbytes = read(fd[0],charbuffer,sizeof(charbuffer) );

   printf("The child process recieves %s", charbuffer);


   //printf("child pid is %d", childpid);

   }

    return 0;
}
