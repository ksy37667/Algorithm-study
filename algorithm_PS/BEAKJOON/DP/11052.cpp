//11052

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<char> alpha;

int main(){
	int N, dp[10001], P[10001];
	
	cin >> N;
	
	for(int i = 1; i<=N; i++){
		cin >> P[i];
	}
	dp[1] = P[1];
	
	for(int i = 2; i<=N; i++){
		for(int j = 1; j<=i; j++){
			dp[i] = max(dp[i],dp[i-j]+P[j]);
			cout << dp[i] << ": " << i << " " << j << endl;
		}
	}
	cout << dp[N];
}
