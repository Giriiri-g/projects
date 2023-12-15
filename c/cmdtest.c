#include <stdio.h>

int main(int argc, char *argv[]){​
	int i, n1, n2;
    printf("No. of arg is %d\n", argc);
    for (i=0; i<argc; ++i) ​
         printf("%s\n", argv[i]);
    sscanf(argv[1], "%d", &n1);
    sscanf(argv[2], "%d", &n2);
    printf("Sum is %d\n", n1 + n2);
    return 0;
}
