#include<iostream>
using namespace std;
int main(){
    int t,a,i;
    char s[100];
    cin>>t;
    while(t--){
        a = 0;
        cin>>s;
        for(i = 0;s[i];i++){
            if(s[i] == 'a')
                a++;
        }
    cout<<min(a,i-a)<<endl;
    } 
    return 0;
}