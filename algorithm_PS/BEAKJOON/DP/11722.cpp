#include <iostream>

using namespace std;

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int N;
	
	cin >> N;
	
	int arr[N+1];
	int cache[N+1];
	
	for(int i = 1; i<=N; i++){
		cin >> arr[i];
		cache[i] = 1;
	}
	
	for(int i = 1; i<=N; i++){
		for(int j = 1; j<=i; j++){
			if(arr[i] < arr[j] && cache[j] +1 > cache[i]){
				cache[i] = cache[j] + 1;
				cout << i << j << endl;
			}
		}
	}
	
	int MAX = 0;
	
	for(int i = 1; i<=N; i++){
		if(cache[i]>MAX){
			MAX = cache[i];
		}
	}
	
	cout << MAX;
}
