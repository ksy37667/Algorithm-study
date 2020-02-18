#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int T;
	
	cin >> T;
	
	for(int test = 0; test<T; test++){
		int N;
		cin >> N;
		
		int arr[101][101];
		int cache[101][101];
		
		memset(arr,0,sizeof(arr));
		memset(cache,0,sizeof(cache));
		
		for(int i = 1; i<=N; i++){
			for(int j = 1; j<=i; j++){
				cin >> arr[i][j];
			}
		}
		cache[1][1] = arr[1][1];
		
		for(int i = 2; i<=N; i++){
			for(int j = 1; j<=i; j++){
				if(j == 1){
					cache[i][j] = arr[i][j]+cache[i-1][j];
				}else if(j==i){
					cache[i][j] = arr[i][j]+cache[i-1][j-1];
				}else{
					cache[i][j] = max(cache[i-1][j-1]+arr[i][j],cache[i-1][j]+arr[i][j]);
				}
			}
		}
		
		int MAX = 0;
		
		for(int i = 1; i<=N; i++){
			if(MAX < cache[N][i]){
				MAX = cache[N][i];
			}
		}
		
		cout << MAX << "\n";
	}
}
