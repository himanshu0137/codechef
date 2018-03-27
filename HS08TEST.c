#include<stdio.h>
int main(){
	float b;
	int w;
	scanf("%d %f",&w,&b);
	if((w+0.5)<=b && w%5==0){
		printf("%.2f\n",b-w-0.5);
	}
	else{
		printf("%.2f",b);
	}
	return 0;
}