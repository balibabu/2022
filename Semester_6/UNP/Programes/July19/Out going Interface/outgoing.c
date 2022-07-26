

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
#define MAXSIZE 2100
#define MAXCLIENT 150

typedef struct sockaddr GSA;
typedef struct sockaddr_in SA;

int main(int argc, char **argv){
	int sockfd;
	socklen_t len;
	struct sockaddr_in cliaddr, servaddr;

	if (argc != 2){
	        fprintf(stderr,"usage %s <IP address >\n", argv[0]);
		exit(1);
	}
	sockfd = socket(AF_INET, SOCK_DGRAM, 0);

	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_port = htons(SERVERPORT);
	servaddr.sin_addr.s_addr = inet_addr(argv[1]);
	connect(sockfd, (GSA *) &servaddr, sizeof(servaddr));

	len = sizeof(cliaddr);
	getsockname(sockfd, (GSA *) &cliaddr, &len);
	printf("local address %s : %d\n", inet_ntoa(cliaddr.sin_addr),ntohs(cliaddr.sin_port));
	exit(0);
}


