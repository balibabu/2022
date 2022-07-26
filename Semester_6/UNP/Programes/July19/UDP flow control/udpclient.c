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
#define NDG 20 /* Datgram to send*/
#define DGLEN 14 /*lenth of data gram*/
void dg_cli(FILE *FP, int sockfd, const struct sockaddr* pservaddr,socklen_t servlen)
{
int i;
char sendline[DGLEN];
memset(sendline,'\0',sizeof(sendline));
while(1)
{
printf("Enter the meassge....\n");
fgets(sendline,200,stdin);
for(i=0;i<NDG;i++)
{
sendto(sockfd,sendline,DGLEN,0,pservaddr,servlen);
}
printf("Data sent....\n");
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
fprintf(stderr,"Usage %s <IP> <PORT>\n", argv[0]);
return 1;
}
servaddr.sin_family=AF_INET;
servaddr.sin_addr.s_addr=inet_addr(argv[1]);
servaddr.sin_port=htons(atoi(argv[2]));
sockfd=socket(AF_INET,SOCK_DGRAM,0);
if(sockfd>0)
{
fprintf(stderr,"Socket create success...\n");
}
else
{
fprintf(stderr,"Create an Error...\n");
return 1;
}
dg_cli(stdin,sockfd,(struct sockaddr*)&servaddr,sizeof(servaddr));
printf("Connected servaer details...\n");
printf("Server Port number%d\n",ntohs(servaddr.sin_port));
printf("Server IP=%s\n",inet_ntoa(servaddr.sin_addr));
getsockname(sockfd,(struct sockaddr*)&cliaddr,&len);
exit(0);
return 0;
}
