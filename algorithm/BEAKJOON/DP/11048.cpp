#include <iostream>

using namespace std;

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int N,M;
	
	cin >> N >> M;
	
	int arr[N+1][M+1] = {};
	int cache[N+1][M+1] = {};
	
	for(int i = 1; i<=N; i++){
		for(int j = 1; j<=M; j++){
			cin >> arr[i][j];
		}
	}
	
	cache[1][1] = arr[1][1];
	
	
	for(int i = 1; i<=N; i++){
		for(int j = 1; j<=M; j++){
			cache[i][j] = max(cache[i-1][j] + arr[i][j], cache[i][j-1]+arr[i][j]);
		}
	}
	
	cout << cache[N][M];
}
