
#include<stdio.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<sys/select.h>
#include<sys/time.h>
#include <errno.h>
#include <signal.h>

#define SERVERPORT 9157
#define MAXSIZE 20
#define MAXCLIENT 150

typedef struct sockaddr GSA;
typedef struct sockaddr_in SA;


void err_sys(const char *x) {
	perror(x);
	exit(EXIT_FAILURE);
}

void dg_send(int sockFd, GSA * cliAddr,socklen_t len) {
	char buffer[MAXSIZE]="Hello Sougata",recvBuffer[MAXSIZE];
	GSA * sa;

	while (1){
		sendto(sockFd, buffer,MAXSIZE,0,cliAddr,len);
		printf("Data sent\n");

//		int n = recvfrom(sockFd, recvBuffer, MAXSIZE, 0, sa, &len);
//		recvBuffer[n]=0;
//		printf("Received : %s\n",recvBuffer);
		printf("any key to resend\n");
		getchar();
		sleep(2);
	}
}

int main(int argc, char *argv[]) {
	int sockFd;
	SA servaddr;

	if(argc !=3){
	        fprintf(stderr,"usage %s <client Ip> <Client port>\n", argv[0]);
		//printf("Usage : <prgName> <client Ip> <Client port>\n");
		exit(EXIT_SUCCESS);
	}

	sockFd = socket(AF_INET, SOCK_DGRAM, 0);
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY); //get ip from server
	servaddr.sin_port = htons(SERVERPORT); // Get the port from the server

	int bindStatus = bind(sockFd, (GSA*) &servaddr,sizeof(servaddr));
	if (bindStatus == -1) {
		perror("Bind");
		exit(EXIT_FAILURE);
	}else
		printf("Server Running on port %d \n",SERVERPORT);

	SA cliAddr;
	cliAddr.sin_family = AF_INET;
	cliAddr.sin_addr.s_addr = inet_addr(argv[1]);
	cliAddr.sin_port = htons(atoi(argv[2]));
	socklen_t len = sizeof(SA);

	dg_send(sockFd,(GSA *)&cliAddr,len);
	printf("Client Terminating...\n");
}


