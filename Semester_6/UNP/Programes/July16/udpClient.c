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

#define SERVERPORT 9156
#define MAXSIZE 1000
typedef struct sockaddr_in SA;
typedef struct sockaddr GSA;


void handle_fun(int signo){
	printf("Signal Raised = %d\n",signo);
	printf("Alarm Raised up: Receive failed\n");
}


void dg_cli(int sockFd,FILE *fp,GSA * sa,socklen_t len){
	char sendBuffer[MAXSIZE], recvBuffer[MAXSIZE];
	int flag;
//	signal(SIGALRM, handle_fun);
	GSA *rep_sa;
	rep_sa = (GSA *)malloc(sizeof(GSA));
	socklen_t rep_len;

	fprintf(stdout,"SEND :");
	while((fgets(sendBuffer, MAXSIZE,fp))!=NULL){
		sendto(sockFd, sendBuffer, strlen(sendBuffer), 0, sa, len);
		printf("Data sent...\n");
		sleep(4);
		flag =0;
		do{
			rep_len = len;
			int n = recvfrom(sockFd, recvBuffer, MAXSIZE, 0, rep_sa,&rep_len);
			recvBuffer[n]=0;
			if((len == rep_len) && (memcmp(sa,rep_sa,len) == 0)){
				flag = 1;
				if(n>0){
					printf("Received from Server:: %s\n",recvBuffer);
				}else if(n==0){
					printf("n becomes zero\n");
					break;
				}else{
					perror("Recvfrom");
					exit(EXIT_FAILURE);
				}
			}else{
				SA * tempSa;
				tempSa = (SA *)rep_sa;
				flag =0;
				printf("Reply from  %s:%d (ignored) | data = %s \n",inet_ntoa(tempSa->sin_addr),ntohs(tempSa->sin_port),recvBuffer);
			}
		}while(flag == 0);

		fprintf(stdout,"SEND :");
	}

}

int main(int argc, char **argv) {
	SA servAddr;
	socklen_t len = sizeof(SA);

	if(argc != 3){
	        fprintf(stderr,"usage %s <IP > <PORT>\n", argv[0]);
		//printf("Usage : <progName> <IP>\n");
		exit(EXIT_SUCCESS);
	}

	int sockFd = socket(AF_INET,SOCK_DGRAM,0);
	if (sockFd == -1){
		perror("Socket");
		exit(EXIT_FAILURE);
	}else{
		printf("Socket created successfully\n");
	}
	bzero(&servAddr, len);
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = inet_addr(argv[1]);
	servAddr.sin_port = htons(SERVERPORT);

	dg_cli(sockFd, stdin, (GSA *)&servAddr, len);
	printf("Client is terminating\n");
	return 0;
}
