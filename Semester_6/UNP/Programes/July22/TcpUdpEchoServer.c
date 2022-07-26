#include<stdio.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<stdlib.h>
#include<string.h>
#include<strings.h>
#include<time.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<sys/select.h>
#include<sys/time.h>
#include <errno.h>
#include <signal.h>

#define SERVERPORT 9156
#define MAXSIZE 200
#define MAXCLIENT 150

typedef struct sockaddr GSA;
typedef struct sockaddr_in SA;

void sig_chld(int signo)
{
}
void err_quit(char *str)
{
perror(str);
exit(EXIT_FAILURE);
}
void str_echo(int connfd)
{
ssize_t n;
char buffer[MAXSIZE];
while((n=read(connfd,buffer,MAXSIZE))>0)
{
buffer[n]=0;
printf("Received(TCP)::%s\n",buffer);
write(connfd,buffer,n);
}
if(n==0)
{
printf("Terminating (TCP)\n");
}
else if(n<0)
{
err_quit("Read");
}
}
int main(int argc, char **argv)
{
int lisnfd,udpfd,connfd,nready,maxfd;
char buffer[MAXSIZE];
pid_t chpid;
fd_set rset;
socklen_t len;
const int on =1;
ssize_t n;
SA servaddr, cliaddr;
len=sizeof(SA);
/* Create TCP Socket*/
lisnfd=socket(AF_INET,SOCK_STREAM,0);
bzero(&servaddr,len);
servaddr.sin_family=AF_INET;
servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
servaddr.sin_port=htons(SERVERPORT);
int bindstatus=bind(lisnfd,(GSA*)&servaddr,len);
if(bindstatus<0)
err_quit("Bind TCP");
else
printf("Bind (TCP) successful..\n");
listen(lisnfd,MAXCLIENT);
/* Create UDP Socket*/
udpfd=socket(AF_INET,SOCK_DGRAM,0);
bindstatus=bind(udpfd,(GSA*)&servaddr,len);
if(bindstatus<0)
err_quit("Bind (UDP)");
else
printf("Bind (UDP) successful...\n");
signal(SIGCHLD,sig_chld);
FD_ZERO(&rset);
maxfd=(lisnfd>udpfd?lisnfd:udpfd)+1;
while(1)
{
FD_SET(lisnfd,&rset);
FD_SET(udpfd,&rset);
nready=select(maxfd,&rset,NULL,NULL,NULL);
if(nready<0)
{
if(errno==EINTR)
continue;
else
err_quit("Select Error..\n");
}
len=sizeof(cliaddr);
if(FD_ISSET(lisnfd,&rset))
{
connfd=accept(lisnfd,(GSA*)&servaddr,&len);
if((chpid=fork())==0)
{
close(lisnfd);
str_echo(connfd);
exit(EXIT_SUCCESS);
}
close(connfd);
}
if(FD_ISSET(udpfd,&rset))
{
n=recvfrom(udpfd,buffer,MAXSIZE,0,(GSA*)&cliaddr,&len);
buffer[n]=0;
printf("Received(UDP)::%s\n",buffer);
sendto(udpfd,buffer,n,0,(GSA*)&cliaddr,len);
}
}
}
