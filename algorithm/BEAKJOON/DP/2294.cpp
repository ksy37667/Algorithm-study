#include <iostream>

using namespace std;

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int N, K, sum;
	
	cin >> N >> K;
	
	int arr[N] = {};
	int cache[K+1] = {};
	
	for(int i = 0; i<N; i++){
		cin >> arr[i];
	}
	
	
	for(int i = 1; i<=K; i++) cache[i] = 10001;
	
	
	for(int i = 0; i<N; i++){
		for(int j = arr[i]; j<=K; j++){
			cache[j] = min(cache[j], cache[j-arr[i]]+1);
		}
	}
	
	if(cache[K] == 10001) cout << -1;
	else{
		cout << cache[K];
	}
	
}
