#include <iostream>

using namespace std;

int sum = 0;
int cnt = 0;

void func(int n, int sum){
	if(sum > n) return ;
	if(sum == n){
		cnt++;
		return ;
	}
	
	for(int i = 1; i<=3; i++){
		func(n,sum+i);
	}
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
    int T;
    
    cin >> T;
    
    for(int test = 0; test < T; test++){
    	int n;
    	cnt = 0;
    	cin >> n;
    	
    	func(n, 0);
    	cout << cnt << "\n";
	}
}
