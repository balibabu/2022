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

void err_quit(const char* x)
{
    perror(x);
    exit(EXIT_FAILURE);
}

void str_cli(FILE *fp, int sockfd)
{
	char exitMssg[10] = "bye";
	char sendline[MAXLINE], recvline[MAXLINE];
	printf("SEND :");
	while (fgets(sendline, MAXLINE, fp) != NULL) {
		sendline[strlen(sendline)-1]=0;
		if(strcmp(sendline, exitMssg)==0){
			return;
		}
		write(sockfd, sendline, strlen (sendline));
		return;

		if (read(sockfd, recvline, MAXLINE) == 0)
			err_quit("str_cli: server terminated prematurely");
		printf("RECIEVED :");
		fputs(recvline, stdout);
		printf("\n");
		printf("SEND :");
	}
}
void print_linger(int sockFd){
	struct linger l;
	int n;
	int len = sizeof(l);
	getsockopt(sockFd, SOL_SOCKET, SO_LINGER, &l, &len);
	printf("l_onoff = %d l_linger = %d\n",l.l_onoff,l.l_linger);

	len=sizeof(n);
	getsockopt(sockFd, SOL_SOCKET, SO_RCVBUF, &n, &len);
	printf("Receive Buffer size: %d\n",n);

	len=sizeof(n);
	getsockopt(sockFd, SOL_SOCKET, SO_SNDBUF, &n, &len);
	printf("Send Buffer size: %d\n",n);

}
#define Max 3999999
int main(int argc, char *argv[]) {
	int sockfd, n, conStatus, len;
	printf("%d\n",Max);
	char recvline[Max];
	struct linger ling;

	struct sockaddr_in servaddr;
	if(argc != 4){
	     fprintf(stderr,"Usage %s <IP> <l_onoff> <l_linger>\n", argv[0]);
		//printf("Usage <IP> <l_onoff> <l_linger>\n");
		exit(EXIT_FAILURE);
	}
	ling.l_onoff = atoi(argv[2]);
	ling.l_linger = atoi(argv[3]);
	len = sizeof(struct sockaddr_in);
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = inet_addr(argv[1]); //get ip from server
	servaddr.sin_port = htons(SERVERPORT); // Get the port from the server

	conStatus = connect(sockfd, (struct sockaddr*) &servaddr, sizeof(servaddr));
	if(conStatus == -1){
		perror("Connect");
		exit(EXIT_FAILURE);
	}
	setsockopt(sockfd,SOL_SOCKET,SO_LINGER,&ling,sizeof(ling));
	print_linger(sockfd);

	printf("conStatus : %d, sockFd : %d\n", conStatus, sockfd);
	str_cli(stdin, sockfd);
	printf("Client Terminating...\n");
	int closeRet = close(sockfd);
//	int closeRet = shutdown(sockfd,SHUT_WR);
	if (closeRet<0){
		perror("close");
	}
	printf("closeRet=%d\n",closeRet);

	int zz=read(sockfd,recvline,Max);
	printf("zz = %d data= %s\n",zz,recvline);
	if(zz<0)
		perror("zz");
}
