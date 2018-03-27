#include<iostream>
using namespace std;
int main(){
	int t;cin>>t;
	while(t--){
		int n,x;cin>>n>>x;
		int ar[n],min=101,sum=0;
		for(int i=0;i<n;i++){
			cin>>ar[i];
			if(ar[i]<min) min=ar[i];
			sum+=ar[i];
		}
		if(sum/x==(sum-min)/x)cout<<-1<<endl;
		else cout<<sum/x<<endl;
	}
}