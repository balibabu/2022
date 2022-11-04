#include <unistd.h>
#include <sys/file.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdio.h>
#include <string.h>

int fd;
off_t read_offset;
int q = 0;

void* reader_routine(void* p)
{
    char buffer[32] = {0};
    int bytesRead = 0;

    while(!q)
    {
        flock(fd, LOCK_EX);
        lseek(fd, read_offset, SEEK_SET);
        bytesRead = read(fd, buffer, 32);
        flock(fd, LOCK_UN);
        if (bytesRead > 0)
        {
            read_offset = lseek(fd, read_offset + bytesRead, SEEK_SET);
            buffer[bytesRead] = 0;
            puts(buffer);
        }
    }

    lseek(fd, read_offset, SEEK_SET);
    bytesRead = read(fd, buffer, 32);
    if (bytesRead > 0)
    {
        buffer[bytesRead] = 0;
        puts(buffer);
    }
    return NULL;
}

int main()
{
    pthread_t th;
    const char* const numbers[] = { "one", "two", "three", "four", "five" };
    fd = open("file.txt", O_RDWR | O_CREAT | O_TRUNC, S_IRWXU | S_IRWXG);
    srand(time(NULL));

    read_offset = lseek(fd, SEEK_SET, 0);
     int err =  pthread_create(&th, NULL, reader_routine, NULL);
    for(int i = 0; i < 5; ++i)
    {
        flock(fd, LOCK_EX);
        sleep(rand()%5);
        lseek(fd, 0, SEEK_END);
        write(fd, numbers[i], strlen(numbers[i]));
        flock(fd, LOCK_UN);
    }
    q = 1;
    pthread_join(th, NULL);
    close(fd);
} 
    // cimpile command - gcc -pthread -o rw readwrite.c 

    // run command - ./rw