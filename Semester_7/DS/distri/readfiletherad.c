#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>

pthread_t tid[3];
pthread_mutex_t lock;

char characters[1024] = "";

readFromFile(int fileNumber)
{
    pthread_mutex_lock(&lock);

    char* firstPart = "file";
    char *secondPart = ".in";

    char fileN[1];

    sprintf(fileN, "%d", fileNumber);



    char * fileName = malloc(1 + strlen(firstPart) + strlen(fileN) + strlen(secondPart));
    strcpy(fileName, firstPart);
    strcat(fileName, fileN);
    strcat(fileName, secondPart);

    FILE *fp;
    int c;

    if (!(fp = fopen(fileName, "rt"))) 
    {
         printf("\nError Opening File\n");
         exit(1);
    }
    while ((c = fgetc(fp)) != EOF) 
    {
         strcat(characters, c);
    }
   fclose(fp);

   pthread_mutex_unlock(&lock);
}

int main(int argc, char** argv) {
    int i = 0;
    int err;

    if (pthread_mutex_init(&lock, NULL) != 0) {
        printf("\n Mutex Init Failed\n");
        return 1;
    }

    while (i < 3) {
        err = pthread_create(&(tid[i]), NULL, readFromFile(i), NULL);
        if (err != 0) {
            printf("\nCan't Create thread :[%s]", strerror(err));
        }
        i++;
    }

    pthread_join(tid[0], NULL);
    pthread_join(tid[1], NULL);
    pthread_join(tid[2], NULL);
    pthread_mutex_destroy(&lock);

    return 0;
}