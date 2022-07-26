//UDP echo client_alarm//
#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<stdlib.h>
#include<string.h>
#include<signal.h>
#include<errno.h>
#define PORT 33456
#define MAXLINE 200
void handfun(int signo)
{
printf("Alarming....\n");
}
void dg_cli(FILE *FP, int sockfd,struct sockaddr* pservaddr, socklen_t servlen)
{
int n;
signal(SIGALRM,handfun);
char sendline[MAXLINE],recvline[MAXLINE+1];
memset(sendline,'\0',sizeof(sendline));
memset(recvline,'\0',sizeof(recvline));
while(1)
{
printf("Enter the message...\n");
fgets(sendline,200,stdin);
sendto(sockfd,sendline,strlen(sendline),0,pservaddr,servlen);
alarm(10);
if((n=recvfrom(sockfd,recvline,MAXLINE,0, NULL,NULL))<0)
{
if(errno==EINTR)
{
printf("n:%d\n",n);
alarm(10);
perror("read");
}
else
printf("Inside else data recieved.....\n");
}
else
{
alarm(0);
recvline[n]='\0';
fputs(recvline,stdout);
}
}
}
int main(int argc, char *argv[])
{
int sockfd;
struct sockaddr_in servaddr,cliaddr;
socklen_t len;
len=sizeof(struct sockaddr_in);
if(argc!=3)
{
fprintf(stderr,"usage%s<IP> <PORT>\n",argv[0]);
return 1;
}
servaddr.sin_family=AF_INET;
servaddr.sin_addr.s_addr=inet_addr(argv[1]);
servaddr.sin_port=htons(atoi(argv[2]));
sockfd=socket(AF_INET,SOCK_DGRAM,0);
if(sockfd>0)
{
fprintf(stderr,"Socket create success.....\n");
}
else
{
fprintf(stderr,"Create an error...\n");
return 1;
}
dg_cli(stdin,sockfd,(struct sockaddr*)&servaddr,sizeof(servaddr));
printf("Connected server details.....\n");
printf("Server PORT number%d\n",ntohs(servaddr.sin_port));
printf("Server IP=%s\n",inet_ntoa(servaddr.sin_addr));
getsockname(sockfd,(struct sockaddr*)&cliaddr,&len);
exit(0);
return 0;
}
