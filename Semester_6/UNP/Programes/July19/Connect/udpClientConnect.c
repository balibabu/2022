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
#define SERVERPORT 9156
#define MAXSIZE 200
#define MAXCLIENT 150

typedef struct sockaddr GSA;
typedef struct sockaddr_in SA;
void err_msg(char * msg){
	perror(msg);
	exit(EXIT_FAILURE);
}

void dg_cli(int sockFd, FILE *fp, GSA *SA, socklen_t len) {
	char sendBuffer[MAXSIZE], recvBuffer[MAXSIZE];
	int conStatus = connect(sockFd,SA,len);
	printf("ConStatus = %d\n",conStatus);

	if(conStatus == -1){
		err_msg("Connect");
	}
	while ((fgets(sendBuffer, MAXSIZE, fp)) != NULL) {
		int x = sendto(sockFd, sendBuffer, strlen(sendBuffer), 0, SA, len);
		int n = recvfrom(sockFd, recvBuffer, MAXSIZE, 0, SA, &len);
		if (n == 0) {
			printf("n is zero\n");
			break;
		} else if (n < 0) {
			printf("n=%d\n", n);
			perror("Recv");
			exit(EXIT_FAILURE);
		} else {
			recvBuffer[n] = 0;
			printf("From Server: %s\n", recvBuffer);
		}
	}
}

int main(int argc, char *argv[]) {
	int sockFd, n, len;
	SA servaddr;
	len = sizeof(SA);

	sockFd = socket(AF_INET, SOCK_DGRAM, 0);
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = inet_addr(argv[1]); //get ip from server
	servaddr.sin_port = htons(SERVERPORT); // Get the port from the server

	dg_cli(sockFd, stdin, (GSA*) &servaddr, len);
	printf("Client Terminating...\n");
}
