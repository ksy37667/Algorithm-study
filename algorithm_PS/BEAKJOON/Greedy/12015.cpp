#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0);
	int N, ans = 0;
	cin >> N;
	
	int x = 0;
	
	vector<int> v;
	v.push_back(-1);
		
	for(int i = 0; i<N; i++){
		cin >> x;
		if(v.back() < x){
			v.push_back(x);
			ans++;
		}else{
			auto it = lower_bound(v.begin(),v.end(),x);
			*it = x;
		}
	}
	cout << ans;
}
