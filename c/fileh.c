#include <stdio.h>
#include <string.h>

int main()
{
    FILE *fptr = fopen("data.txt","w");
    char str[] = "C programming";
    int i=0;
    while(i<strlen(str))
    {
        putc(str[i],fptr);
        i++;
    }
    fclose(fptr);
    fptr=fopen("data.txt","r");
    char c;
    while((c=getc(fptr))!=EOF)
    {
        printf("%c",c);
    }
    fclose(fptr);
    return 0;    
}
