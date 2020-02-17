#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int N;
	cin >> N;
	
	int d,w;
	vector<pair <int,int> > v;
	priority_queue<int, vector<int>, greater<int> > pq;
	
	for(int i = 0; i<N; i++){
		cin >> d >> w;
		v.push_back(make_pair(d,w));
	}
	
	sort(v.begin(),v.end());
	
	for(int i = 0; i<N; i++){
		if(pq.size() < v[i].first){
			pq.push(v[i].second);
		}else{
			if(pq.top()<v[i].second){
				pq.pop();
				pq.push(v[i].second);
			}else{
				continue;
			}
		}
	}
	int sum = 0;
	int size = pq.size();
	
	for(int i = 0; i<size; i++){
		sum += pq.top();
		pq.pop();
	}
	
	cout << sum;
}
