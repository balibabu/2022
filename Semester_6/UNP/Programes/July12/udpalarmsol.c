#include<stdio.h>
#include<stdlib.h>
#include<arpa/inet.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<unistd.h>
#include<string.h>
#include<netinet/in.h>
#include<signal.h>
#include<sys/select.h>
#include<wait.h>
typedef struct sockaddr_in SA;
typedef struct sockaddr GSA;
#define MAXCLIENT 10
#define MAXSIZE 1000
#define SERVPORT 9156
int redAvailable(int fd,int sec)
{
fd_set rset;
struct timeval t;
FD_ZERO(&rset);
FD_SET(fd,&rset);
t.tv_sec =sec;
t.tv_usec=0;
return(select(fd+1,&rset,NULL,NULL,&t));
}
void sig_alrm(int signo)
{
printf("Alarm Raised......\n");
}
void dg_cli(int sockfd,FILE *fp,GSA* servaddr,socklen_t len)
{
int n;
signal(SIGALRM, sig_alrm);
char sendline[MAXSIZE],recvline[MAXSIZE];
while(fgets(sendline,MAXSIZE,fp)!=NULL)
{
int x=sendto(sockfd,sendline,strlen(sendline),0, servaddr,len);
printf("Send to returns:%d\n",x);
x=redAvailable(sockfd,5);
printf("Return of the select %d\n", x);
if(x==0)
{
printf("socket time out...\n");
}
else if(x<0)
{
perror("Error....\n");
}
else
{
n=recvfrom(sockfd,recvline,MAXSIZE,0,servaddr,&len);
printf("Recvfrom returns:%d\n",n);
if(n==-1)
{
perror("Read error");
}
else if(n==0)
{
break;
}
recvline[n]=0;
printf("Received from server....");
fputs(recvline,stdout);
}
}
}
int main(int argc, char*argv[])
{
int sockfd,n,conStatus,len;
char recvline[1024];
SA servaddr,cliaddr;
if(argc!=3)
{
fprintf(stderr,"Usage %s <IP> <PORT>\n",argv[0]);
exit(EXIT_FAILURE);
}
len=sizeof(SA);
sockfd=socket(AF_INET,SOCK_DGRAM,0);
servaddr.sin_family=AF_INET;
servaddr.sin_addr.s_addr=inet_addr(argv[1]);
servaddr.sin_port=htons(atoi(argv[2]));
dg_cli(sockfd,stdin,(GSA*)&servaddr,sizeof(servaddr));
printf("Terminating Client...\n");
close(sockfd);
}
