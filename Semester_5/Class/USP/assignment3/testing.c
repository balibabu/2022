#include <stdio.h>
#include <stdlib.h>
int main() {
    char choice;
    char *command;
    command  = (char *) malloc(sizeof(char) * 100);
    do {
        printf("Do you want to enter more commands (y/n)");
        scanf("%c", &choice);
        if(choice == 'y') {
            printf("Enter the command\n");
            scanf("%s", command);
            getchar();
            system(command);
        }
    } while(choice == 'y');
    return 0;
}