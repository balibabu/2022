#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>


void function(int sockfd){
	int size,maximum;
	int array[100];
	printf("enter the size of array: ");
	scanf("%d",&size);
	array[0]=size; //first element is size of array
	printf("enter the elements in the array\n");
	for(int i=1;i<=size;i++){
		scanf("%d",&array[i]);
	}
	write(sockfd,array,sizeof(array));
	read(sockfd,&maximum,sizeof(maximum));
	printf("the maximum number is %d\n",maximum);
}


int main(){
	int sockfd;
	struct sockaddr_in servAddr;
	servAddr.sin_addr.s_addr=inet_addr("127.0.0.1");
	servAddr.sin_family=AF_INET;
	servAddr.sin_port=htons(5555);
	sockfd=socket(AF_INET,SOCK_STREAM,0);
	connect(sockfd,(struct sockaddr*)&servAddr,sizeof(servAddr));

    function(sockfd);
	printf("closing socket...\n");
	close(sockfd);
	return 0;
}