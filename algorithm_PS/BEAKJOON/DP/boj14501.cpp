#include <iostream>
#include <string.h>

using namespace std;
int  N;

int arr[2][15];
bool ck[15] = {};
int cache[15];


int func(int k){
	cout << k << " : "<<cache[k] << " " << "\n";
	if(k == N) return 0;
	if(k > N) return -987654321;
	if(cache[k] != -1) return cache[k];
	return cache[k] = max(func(k+1) , func(k+arr[0][k])+arr[1][k] );
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
	memset(cache,-1,sizeof(cache));
    cin >> N;
    
    for(int i = 0; i<N; i++){
    	cin >> arr[0][i] >> arr[1][i];
	}
	func(0);


	cout << func(0);
}
