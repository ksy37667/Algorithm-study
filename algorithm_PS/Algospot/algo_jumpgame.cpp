#include <iostream>
#include <string.h>

using namespace std;

int n,board[100][100];
int cache[100][100];
int jump2(int y, int x){
	if(y>=n||x>=n) return 0;
	if(y == n-1 && x == n-1) return 1;

	if(cache[y][x]!= -1) return cache[y][x];
	int jumpSize = board[y][x];
	return cache[y][x] = (jump2(y + jumpSize, x) || jump2(y,x+jumpSize));
}

int main(){
	
	
	int T;
	cin >> T;
	for(int test = 0; test<T; test++){
		cin >> n;
		memset(cache,-1,sizeof(cache));
		for(int i = 0; i<n; i++){
			for(int j = 0; j<n; j++){
				cin >> board[i][j];
			}
		}
		
		if(jump2(0,0)==1){
			cout << "YES" << "\n";
		}else{
			cout << "NO" << "\n";
		}
	}

}
