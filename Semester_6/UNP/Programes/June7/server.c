#include<stdio.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
int main(int argc, char **argv)
{
    int listenfd,connfd,len;
    struct sockaddr_in servaddr,clientaddr;
    char buff[1024];
    time_t ticks;
    len=sizeof(struct sockaddr_in);
    listenfd=socket(AF_INET,SOCK_DGRAM,0);
    servaddr.sin_family=AF_INET;
    servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
    servaddr.sin_port=htons(0);
    bind(listenfd,(struct sockaddr *)&servaddr, sizeof(servaddr));
    getsockname(listenfd, (struct sockaddr *)&servaddr, &len);
    printf("After bind ephemeral port=%d\n",(int)ntohs(servaddr.sin_port));
    listen(listenfd,5);
    connfd=accept(listenfd, (struct sockaddr *)&clientaddr,&len);
    ticks=time(NULL);
    snprintf(buff,sizeof(buff),"%s\r\n",ctime(&ticks));
    write(connfd,buff,strlen(buff));
    write(connfd,"ITER",4);
    close(connfd);
}
