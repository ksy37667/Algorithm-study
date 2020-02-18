#include <iostream>
#include <stdlib.h>

using namespace std;

int N , mini = 987654321;
int arr[20][20];
bool ck[20] = {};


void func(int dept, int k){
	if(dept == N/2){
		int start, link;
		start = link = 0;
		
		for(int i = 0; i<N; i++){
			for(int j = 0; j<N; j++){
				if(ck[i] && ck[j]) start += arr[i][j];
				if(!ck[j] && !ck[i]) link +=arr[i][j];
			}
		}
		
		if(mini > abs(start-link)){
			mini = abs(start-link);
		}
		
		return ;
	}
	for(int i = k; i<N-1; i++){
		ck[i] = true;
		func(dept+1, i+1);
		ck[i] = false;
	}
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
	cin >> N;
	
	for(int i = 0; i<N; i++){
		for(int j = 0; j<N; j++){		
			cin >> arr[i][j];
		}
	}
	
	
	func(0,0);

	cout << mini;
}


