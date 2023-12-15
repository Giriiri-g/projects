#include <stdio.h>

void rshift(int *arr){
    int temp1=0, temp2;
    for (int i=0; i<sizeof(arr)/2;i++){
        temp2 = arr[i];
        arr[i]=temp1;
        temp1=temp2;
    }
}

int main()
{
    int ar[4]= {1, 2, 3 ,4};
    rshift(ar);
    for (int i=0; i<(sizeof(ar)/2);i++){
        printf("%d", ar[i]);
    }
    return 0;
}
