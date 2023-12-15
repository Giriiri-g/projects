// Girish S, AM.EN.U4AIE22044
#include <stdio.h>
int q1(){
	int m, n;
    printf("Enter the dimensions of the first matrix :");
    scanf("%d%d", &m, &n);
    int arr[m][n];
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            scanf("%d", &arr[i][j]);
        }
    }
	printf("Enter values for the second matrix :\n");
    int arr1[m][n];
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            scanf("%d", &arr1[i][j]);
        }
    }
    int arr3[m][n];
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            arr3[i][j] = arr[i][j] + arr1[i][j];
        }
    }
	printf("\n\n");
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            printf("%d   ", arr3[i][j]);}
        printf("\n");}
    return 0;
	}





int q2()
{
    int m, n;
    printf("Enter the dimensions of the matrix :");
    scanf("%d%d", &m, &n);
    int arr[n][m];
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            scanf("%d", &arr[i][j]);
        }
    }
    int out[m], sum=0;
    for (int i=0; i<m; i++){
        sum=0;
        for (int j=0; j<n; j++){
            sum+=arr[i][j];
        }
        out[i]=sum;
    }
	printf("\n\n");
    for (int i=0; i<m; i++){
        printf("%d   ", out[i]);}
    return 0;
}


int q3(){
	int m, n;
    printf("Enter the dimensions of the matrix :");
    scanf("%d%d", &m, &n);
    int arr[m][n];
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            scanf("%d", &arr[i][j]);
        }
    }
    int temp;
    for (int i=0; i<n; i++){
		temp = arr[1][i];
		arr[1][i] = arr[0][i];
		arr[0][i] = temp;}
	printf("\n\n");
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            printf("%d   ", arr[i][j]);}
        printf("\n");}
	return 0;}


int q4(){
	int m, n;
    printf("Enter the dimensions of the matrix :");
    scanf("%d%d", &m, &n);
    int arr[m][n];
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            scanf("%d", &arr[i][j]);
        }
    }
    int r, s;
    printf("Enter the rth row and scalar to multiply :");
    scanf("%d%d", &r, &s);
    for (int i=0; i<n; i++){
		arr[r][i] = arr[r][i]*s;}
    for (int i=0; i<m; i++){
        for (int j=0; j<n; j++){
            printf("%d   ", arr[i][j]);}
        printf("\n");}
	return 0;}
int main(){
	/*q1();
	q2();
	q3();*/
	q4();
	return 0;}
