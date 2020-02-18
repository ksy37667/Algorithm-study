#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int N;
	vector<pair <int,int> > v;
	cin >> N;
	
	for(int i = 0; i<N; i++){
		int S , T;
		cin >> S >> T;
		v.push_back(make_pair(S,T));	
	}
	
	sort(v.begin(), v.end());
	
	priority_queue<int, vector<int>, greater<int> > pq;
	
	pq.push(v[0].second);
	
	for(int i = 1; i<N; i++){
		if(pq.top() > v[i].first){
			pq.push(v[i].second);
		}else{
			pq.pop();
			pq.push(v[i].second);
		}
	}
	
	cout << pq.size();
}
