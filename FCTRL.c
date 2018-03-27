#include<stdio.h>
int fun(int x,int y){
	int c=0,t,q=y;
	while(1){
		t = x/q;
		if(t)
			c += t;
		else
			break;
		q*=y;
	}
	return c;
}
int main(){
	int t,c2,c5;
	unsigned long int a;
	scanf("%d",&t);
	while(t--){
	scanf("%d",&a);
	c2 = fun(a,2);
	c5 = fun(a,5);
	if(c2 <= c5){
		printf("%d\n",c2);
	}
	else{
		printf("%d\n",c5);
	}
	}
	return 0;
}