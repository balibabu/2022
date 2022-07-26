#include<stdio.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<arpa/inet.h>
#include<unistd.h>

#define SERVERPORT 9156
#define MAXLINE 2000
#include <errno.h>
//#include "str_echo.cb"


void err_sys(const char* x)
{
    perror(x);
    exit(EXIT_FAILURE);
}

void str_echo(int sockfd){
	ssize_t n;
	char buf[MAXLINE];
	int count = 0;

	do{
		 while (( n = read(sockfd, buf, MAXLINE)) > 0 ){
			 buf[n]=0;
			 printf("Server (%d) n=%ld data=%s\n",++count,n,buf);
			 write(sockfd, buf, n+1);
		 }

	}while (n < 0 && errno == EINTR);
	if ( n < 0 )
		err_sys("str echo : read error");
	printf("n=%ld\n",n);
}

//void str_echo(int sockfd);

int main(int argc, char **argv) {
	int listenfd, connfd, len;
	struct sockaddr_in servaddr, clientaddr;
	char buff[1024];
	pid_t childPid;
	const int on = 1;
	len = sizeof(struct sockaddr_in);
	printf("ppid = %ld\n",(long)getpid());

	listenfd = socket(AF_INET, SOCK_STREAM, 0);
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servaddr.sin_port = htons(SERVERPORT);

	setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR, &on, sizeof(on));
	int bindStatus = bind(listenfd, (struct sockaddr*) &servaddr, sizeof(servaddr));
	if (bindStatus == -1){
		perror("Bind");
		exit(EXIT_FAILURE);
	}
//	int sockStatus = getsockname(listenfd, (struct sockaddr*) &servaddr, &len);
//	printf("Socket Name Status : %d\n", sockStatus);
	printf("After bind ephemeral port =%d , bindStatus = %d, listenfd = %d\n\n", (int) ntohs(servaddr.sin_port),bindStatus,listenfd);
	listen(listenfd, 5);

	while (1){
		connfd = accept(listenfd, (struct sockaddr*) &clientaddr, &len);
		if((childPid = fork())== 0){    /*Child Process*/
			printf("pid = %ld\n",(long)getpid());
			printf("Received Request From : %s | confd = %d | listenfd=%d\n", inet_ntoa(clientaddr.sin_addr),connfd,listenfd);
			close(listenfd);
			printf("sleeping 10 sec\n");

			sleep(10);
			printf("Awake\n");
			str_echo(connfd);
			printf("Child Server Terminating...\n");
			close(connfd);
			exit(EXIT_SUCCESS);
		}
		close(connfd);
	}
}
