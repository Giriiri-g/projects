#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void display(int arr[], int size){
	for (int i=0; i<size; i++){
		printf("%d ", arr[i]);
		}}

int linsearch(int arr[], int size, int num){
	for(int i=0; i<size; i++){
		if (num==arr[i]) return 1;}
	return 0;}

void swap(int *arr, int ind1, int ind2){
	int temp=arr[ind1];
	arr[ind1]=arr[ind2];
	arr[ind2]=temp;}

void reverse(int *arr, int size){
	for(int i=0; i<size/2; i++){
		int temp = arr[i];
		arr[i]=arr[size-1-i];
		arr[size-i-1]=temp;}	
	}

void pop(int *arr, int size, int index){
	if (index>=size || index<0){
		printf("Index out of range");
		return;}
	for(int i=index+1; i<size; i++){
		arr[i-1]=arr[i];}
	arr = realloc(&arr, 4);
}
void printwrd(char *s, int size){
	int wstart=0;
	for(int i=0; i<size; i++){
		if(s[i]==' '){
			for(int j=wstart; j<i; j++){
				printf("%c", s[j]);}
			wstart=i+1;
			printf("\n");
			}
	}
	for(int j=wstart; j<size; j++){
		printf("%c", s[j]);}
}
int main(){
	int *arr = (int *)malloc(2*4);
	for(int i=0; i<2; i++){
		scanf("%d", arr+i);}
	display(arr, 2);
	pop(arr, 2, 1);
	printf("\n%lld\n", sizeof(arr));
	display(arr, 2);
	free(arr);
	return 0;}
