#include<pthread.h>
#include<unistd.h>

int main()
{

 pthread_mutex_t rw;
 pthread_mutex_lock(&rw); 


  return 0;  
}