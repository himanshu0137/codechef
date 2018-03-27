#include<stdio.h>
#define MAX 500
int mult(int x,int res[],int res_size){
	int i,carry = 0;
	for(i=0;i<res_size;i++){
		int prod = res[i]*x+carry;
		res[i]=prod%10;
		carry=prod/10;
	}
	while(carry){
		res[res_size]=carry%10;
		carry/=10;
		res_size++;
	}
	return res_size;
}
void fact(int a){
	int i,res[MAX];
	res[0]=1;
	int res_size=1;
	for(i=2;i<=a;i++)
		res_size=mult(i,res,res_size);
	for(i=res_size-1;i>=0;i--)
		printf("%d",res[i]);
	printf("\n");
}
int main(){
	int t,a;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&a);
		fact(a);
	}
	return 0;
}