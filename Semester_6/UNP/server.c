#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <net.inet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
int main(int argc,char **argv){
	int listenfd,connfd,len;
    struct sockaddr_in servaddr,clientaddr;
    char buff[1024];
    time_t ticks;
    len=sizeof(struct sockaddr_in);
    listenfd=socket(AF_INET,SOCK_STREAM,0);
    servaddr.sin_family=AF_INET;
    servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
    
}