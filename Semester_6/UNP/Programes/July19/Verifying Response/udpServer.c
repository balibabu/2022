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
#define MAXSIZE 20
#define MAXCLIENT 150

typedef struct sockaddr GSA;
typedef struct sockaddr_in SA;


void err_sys(const char *x) {
	perror(x);
	exit(EXIT_FAILURE);
}


void dg_echo(int sockFd) {
	char buffer[MAXSIZE];
	SA cliAddr;
	socklen_t len=sizeof(SA);
	int n;

	while((n = recvfrom(sockFd, buffer,MAXSIZE,0,(GSA *)&cliAddr,&len))>0){
		buffer[n]=0;
		printf("Client Details %s:%d Content = %s\n",inet_ntoa(cliAddr.sin_addr),ntohs(cliAddr.sin_port),buffer);
		sendto(sockFd, buffer,MAXSIZE,0,(GSA *)&cliAddr,len);
	}
	if(n<0)
		err_sys("Recvfrom");
	if (n==0)
		printf("n = 0");
}

int main(int argc, char *argv[]) {
	int sockFd;
	SA servaddr;
	socklen_t len = sizeof(SA);

	sockFd = socket(AF_INET, SOCK_DGRAM, 0);
	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servaddr.sin_port = htons(SERVERPORT);


	int bindStatus = bind(sockFd, (GSA*) &servaddr,sizeof(servaddr));
	if (bindStatus == -1) {
		perror("Bind");
		exit(EXIT_FAILURE);
	}else
		printf("Server Running on port %d \n",ntohs(servaddr.sin_port));

	dg_echo(sockFd);
	printf("Client Terminating...\n");
}
