#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<strings.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<unistd.h>
#include<arpa/inet.h>
#include<netinet/in.h>
#include<errno.h>
#include<signal.h>
#include<sys/wait.h>
#define PORT 33456
#define MAXLINE 200
static void recvfrom_int(int);
static int count;
void dg_echo(int sockfd, struct sockaddr* pclient,socklen_t client)
{
socklen_t len;
char mesg[MAXLINE];
signal(SIGINT,recvfrom_int);
int n;
for(;;)
{
len=client;
n=recvfrom(sockfd,mesg,MAXLINE,0,pclient,&len);
count++;
printf("Message from client%s\n", mesg);
sendto(sockfd,mesg,n,0,pclient,len);
}
}
static void recvfrom_int(int signo)
{
printf("Received %d datagram\n", count);
exit(0);
}
int main()
{
int lisnfd, br;
socklen_t client,len;
struct sockaddr_in servaddr,cliaddr;
len=sizeof(servaddr);
servaddr.sin_family=AF_INET;
servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
servaddr.sin_port=htons(PORT);
lisnfd=socket(AF_INET,SOCK_DGRAM,0);
if(lisnfd<0)
{
fprintf(stderr,"Create error in socket..\n");
return 1;
}
br=bind(lisnfd,(struct sockaddr*)&servaddr,sizeof(servaddr));
if(br==0)
{
printf("Bind Success:with return value=%d\n",br);
}
else
{
printf("Bind unsuccess:with return value=%d\n",br);

printf("Retry.....\n");
exit(2);
}
dg_echo(lisnfd,(struct sockaddr*)&cliaddr,sizeof(cliaddr));
printf("Connected client details....\n");
printf("Client port number=%d\n",ntohs(cliaddr.sin_port));
printf("Client IP details=%s\n",inet_ntoa(cliaddr.sin_addr));
return 0;
}
