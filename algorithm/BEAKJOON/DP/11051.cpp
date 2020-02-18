#include <iostream>
#include <cstring>

using namespace std;

int cache[1000][1000];

int bino(int n, int r){
	if(r == 0 || n == r) return 1;
	if(cache[n][r] != -1) return cache[n][r]%10007;
	return cache[n][r] = bino(n-1,r-1) + bino(n-1,r);
}

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int N,R;
	
	memset(cache,-1,sizeof(cache));
	
	cin >> N >> R;
	
	cout << bino(N,R)%10007;
}
