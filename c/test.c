#include <stdio.h>

int oddoreven()
{
    int x;
    printf("Enter your number :");
    scanf("%d", &x);
    if (x==0)
        printf("The number is 0, it is neither even nor odd");
    else if (x%2==0)
        printf("The number is Even");
    else
        printf("The number is odd");
    return 0;
}

int largest()
{
    int a, b, c;
    printf("\nEnter the three numbers :");
    scanf("%d%d%d", &a, &b, &c);
    if (a>b && a>c)
        printf("The first number is largest\n");
    else if (b>a && b>c)
        printf("The second number is largest\n");
    else
        printf("The third number is largest\n");
    return 0;
}

int validyr()
{
    int year;
    printf("\nEnter the year :");
    scanf("%d", &year);
    if (year%400==0)
        printf("It is a Leap Year!\n");
    else if (year%4 == 0)
    {
        if (year%100 == 0)
            printf("It is not a Leap Year!\n");
        else
            printf("It is a Leap Year!\n");
    }
    else
        printf("It is not a Leap Year!\n");
    return 0;
}

int quad()
{
    int x, y;
    printf("Enter the coordinates :");
    scanf("%d%d", &x, &y);
    if (x<0)
    {
        if (y<0)
            printf("It is in Third Quadrant");
        else
            printf("It is in Second Quadrant");
    }
    else
    {
        if (y<0)
            printf("It is in Fourth Quadrant");
        else
            printf("It is in First Quadrant");
    }
    return 0;
}

int exam()
{
    int roll;
    char name[20];
    float chem, phy, cs;
    printf("\nInput the Roll Number of the student :");
    scanf("%d", &roll);
    printf("\nInput the Name of the Student :");
    scanf("%s", name);
    printf("\nInput the marks of Physics, Chemistry and Computer Application : ");
    scanf("%f%f%f", &chem, &phy, &cs);
    float marks = (chem+phy+cs);
    printf("\nRoll No : %d", roll);
    printf("\nName of Student : %s", name);
    printf("\nMarks in Physics : %f", phy);
    printf("\nMarks in Chemistry : %f", chem);
    printf("\nMarks in Computer Application : %f", cs);
    printf("\nTotal Marks = %f", marks);
    printf("\nPercentage = %f", marks/3);
    if ((marks/3)<40)
        printf("Grade= Fail.");
    else if ((marks/3)<50)
        printf("Grade= Pass.\n");
    else if ((marks/3)<60)
        printf("Grade= D grade.\n");
    else if ((marks/3)<70)
        printf("Grade= C grade.\n");
    else if ((marks/3)<80)
        printf("Grade= B grade.\n");
    else if ((marks/3)<90)
        printf("Grade= A grade.\n");
    else
        printf("Grade= O grade.\n");
    return 0;
}

int bill()
{
    int id;
    float unit, cost, rate, surch;
    char name[30];
    printf("\nEnter the customer ID :");
    scanf("%d", &id);
    printf("\nEnter the name of the customer :");
    scanf("%s", name);
    printf("\nEnter the number of units consumed by the customer :");
    scanf("%f", &unit);
    printf("\nCustomer IDNO :%d", id);
    printf("\nCustomer Name :%s", name);
    printf("\nunit Consumed :%f", unit);
    if (unit<200)
        rate = 1.20;
    else if (unit<400)
        rate = 1.50;
    else if (unit<400)
        rate = 1.80;
    else
        rate = 2.00;
    cost = unit*rate;
    printf("\nAmount Charges @Rs.%f per unit : %f", rate, cost);
    if (cost>400.0)
        surch = cost*15/100;
    else
        surch = 0;
    printf("\nSurchage Amount : %f", surch);
    printf("\nNet Amount Paid By the Customer : %f", (surch+cost));
    return 0;
}

int month2days()
{
    int mth;
    printf("\nEnter the month number :");
    scanf("%d", &mth);
    switch (mth)
    {
        case 1: printf("\n31 days in month %d", mth); break;
        case 2: printf("\n28 days in month %d", mth); break;
        case 3: printf("\n31 days in month %d", mth); break;
        case 4: printf("\n30 days in month %d", mth); break;
        case 5: printf("\n31 days in month %d", mth); break;
        case 6: printf("\n30 days in month %d", mth); break;
        case 7: printf("\n31 days in month %d", mth); break;
        case 8: printf("\n31 days in month %d", mth); break;
        case 9: printf("\n30 days in month %d", mth); break;
        case 10: printf("\n31 days in month %d", mth); break;
        case 11: printf("\n30 days in month %d", mth); break;
        case 12: printf("\n31 days in month %d", mth); break;
        default: printf("\nInvalid Input"); break;
    }
    return 0;
}

int sumchk()
{
    int aa, bb, cc, tt;
    int i =0;
    printf("\nEnter the nuber of test case :");
    scanf("%d", &tt);
    for(i=0; i<tt; i++){
        printf("\nEnter the values for aa, bb, cc :");
        scanf("%d%d%d", &aa, &bb, &cc);
        if (aa== bb+cc)
            printf("\nYes");
        else if (bb == aa+cc)
            printf("\nYes");
        else if (cc == aa+bb)
            printf("\nYes");
        else
            printf("\nNo");
    }
    return 0;
}

int fact()
{/* there is no of test cases -> t, there is a number n -> prime, find m, constraint : m+n is not prime;   in -> t, n  ;  out -> m*/
	int t, n, m=2, x=1, x2=0, j, k, i, v=1;
	printf("Enter the number of test case :");
	scanf("%d", &t);
	for(i=0; i<t; i++){
		m=2;
		printf("\nEnter a Prime number :");
		scanf("%d", &n);
		while (v==1){
			x=1;
			x2=0;
			for (j=2; j<=(int)(m/2); j++){
				if (m%j==0){
					x=0;
					break;}
			}
			if (x==1){
				for (k=2; k<=(int)((m+n)/2); k++){
					if ((m+n)%k==0){
						x2=1;
						break;}
					}
				if (x2==1){
					printf("\n%d", m);
					break;}
				}
			m+=1;}
	}
	return 0;
}

int main()
{
	
    oddoreven();
    largest();
    validyr();
    quad();
    exam();
    bill();
    month2days();
    sumchk();
    fact();
	return 0;
}
