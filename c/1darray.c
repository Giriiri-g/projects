#include <stdio.h>


int q1(){
	int m;
    printf("Enter the dimension of the matrix :");
    scanf("%d", &m);
    int arr[m+1];
    for (int i=0; i<m; i++){
		scanf("%d", &arr[i]);}
	printf("\n");
	int elem, loc, temp1;
	printf("Enter the element and the location :");
	scanf("%d%d", &elem, &loc);
	temp1=arr[loc];
	arr[loc]=elem;
	for (int i=loc+1; i<m+1; i++){
		elem=temp1;
		temp1=arr[i];
		arr[i]=elem;
		}
	for (int i=0; i<m+1; i++){
		printf("%d ", arr[i]);}
	return 0;}
	
int main(){
	q1();
	return 0;}
