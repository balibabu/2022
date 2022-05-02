#include <stdio.h>
#include <string.h>
void is_anagrams(char *str1,char *str2){
    int c=0;
    for(int i=0;str1[i]!='\0' && str2[i]!='\0';i++)
        c^=str1[i]^str2[i];
    printf("%d\n",c);
    
    
}
int main(){
    char str1[100]="king",str2[100]="inkg";
    // str1[0]^=str2[0];
    // str1[1]^=str2[1];
    // str1[2]^=str2[2];
    // printf("%s\n",str1);
    // printf("%d\n",str1[0]);
    // printf("%d\n",str1[1]);
    // printf("%d\n",str1[2]);
    
    // printf("enter a word\n");
    // scanf("%[^\n]s",str1);
    // getchar();
    // printf("enter a word\n");
    // scanf("%[^\n]s",str2);
    is_anagrams(str1,str2);
    return 0;
} 

/*

    public static void main(String[] args) {
        long t1 = System.currentTimeMillis();
        String word = "abcd";
        Arrange("", word);
        System.out.println("\nTotal possibilities " + counter);
        System.out.println("Total time taken " + (System.currentTimeMillis() - t1) + " miliseconds");

    }

    static void Arrange(String str, String word) {
        if (word.length() == 1) {
            System.out.println(str + word);
            counter++;
        } else {

            for (int i = 0; i < word.length(); i++) {
                String temp = word.substring(0, i) + word.substring(i + 1, word.length());
                Arrange(str + word.charAt(i), temp);
            }
        }
    }
*/