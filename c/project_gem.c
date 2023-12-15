#include <stdio.h>
#include <stdlib.h>

void swap_rows(float arr[3][4], int i, int j){
    for (int k=0; k<4; k++){
        float temp=arr[i][k];
        arr[i][k]=arr[j][k];
        arr[j][k]=temp;
    }
}

void multp(float arr[3][4], int i, float num){
    for (int k=0; k<4; k++){
        arr[i][k]*=num;
    }
}

void add(float arr[3][4], int i, int j, float num){
    for (int k=0; k<4; k++){
        arr[i][k]+=num*arr[j][k];
    }
}
void proccess(float arr[3][4]){
    int cnt=0;
    for (int r=0; r<3; r++) {
        if (cnt>=4) {
            return;
        }
        int i=r;
        while (arr[i][cnt]==0) {
            i++;
            if (i==3) {
                i=r;
                cnt++;
                if (cnt==4) {
                    return;
                }
            }
        }
        swap_rows(arr, i, r);
        multp(arr, r, 1.0 / arr[r][cnt]);
        for (int j=0; j<3; j++) {
            if (j!=r) {
                add(arr, j, r, -arr[j][cnt]);
            }
        }
        cnt++;
    }
}

void display(float arr[][100], int rows, int cols) {
    for(int i=0; i<rows; i++) {
        for(int j=0; j<cols; j++)
            printf("%.1f\t", arr[i][j]);
        printf("\n");
    }
}

int cons(float arr[100][100], int rows, int cols){
    for(int i=0; i<rows; i++){
        int cnt=0;
        for(int j=0; j<cols; j++){
            if (arr[i][j]==0) cnt++;
        }
        if (arr[i][cols-1]!=0 && cnt==3) return 1;}
    return 0;
}

void soln(float arr[100][100], int rows, int cols) {
    for (int i=0; i<rows; i++){
        float solution = arr[i][cols-1];
        for(int j=0; j<cols-1; j++){
            if(arr[i][j]!=0){
                printf("x%d = %.1f, ", j+1, solution);
                break;
            }
        }
    }
    printf("\n");
}

int main() {
	int rows, cols;
    float arr[100][100];

    printf("Enter the number of rows and columns of the matrix: ");
    scanf("%d%d", &rows, &cols);

    printf("Enter the elements of the matrix: \n");
    for(int i=0; i<rows; i++){
        for (int j=0; j<cols; j++){
            scanf("%f", &arr[i][j]);}}

    printf("Original matrix:\n");
    display(arr, rows, cols);
    proccess(arr);
    printf("Reduced row echelon form:\n");
    display(arr, rows, cols);
    if(cons(arr, rows, cols)==0){
    printf("It is consistent!\n");
    printf("Solutions:\n");
    soln(arr, rows, cols);}
    else printf("It is Inconsistent!");
    return 0;
}
