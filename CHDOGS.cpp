#include<iostream>
#include<math.h>
using namespace std;
int main(){
	int t;
	double s,v,r;
	cin>>t;
	while(t--){
		cin>>s>>v;
		r = (2*s)/(3*v);
		r = ceil(r*1000000)/1000000;
		cout<<r;
	}
	return 0;
}