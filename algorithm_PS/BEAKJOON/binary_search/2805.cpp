#include <iostream>

using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
    cin.tie(0);
    
	int A,B,V;
	
	cin >> A >> B >> V;
	int cnt = 1;
	int sum = 0;
	while(1){
		
		if(sum + A >= V) {
			cout << cnt; 
			break;	
		}else{
			sum = sum + A - B;
		}
		cnt++;
	}
}


