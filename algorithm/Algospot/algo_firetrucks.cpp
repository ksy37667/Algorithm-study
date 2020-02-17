#include <iostream>
#include <queue>
#include <vector>
#include <memory.h>

using namespace std;
const int INF = 101;

int V,E,N,M;
vector<pair <int, int> > adj[1001];

vector<int> dijkstra(int start){
	vector<int> dist(V, INF);
	dist[start] = 0;
	
	priority_queue<pair<int,int>, vector<pair<int,int> >, greater<pair<int,int> > > pq;
	pq.push(make_pair(0,start));
	
	while(!pq.empty()){
		int cost = pq.top().first;
		int here = pq.top().second;
		
		pq.pop();
		
		if(dist[here] < cost) continue;
		
		for(int i = 0; i<adj[here].size(); i++){
			int there = adj[here][i].first;
			int nextDist = cost + adj[here][i].second;
			if(dist[there] > nextDist){
				dist[there] = nextDist;
				pq.push(make_pair(nextDist,there));
			}
		}
	}
	
	return dist;
}

int main(){
	int T;
	cin >> T;
	
	for(int test = 0; test<T; test++){
		V = 0; E = 0; N = 0; M = 0;
		
		cin >> V >> E >> N >> M;
	
		V++;
		
		vector<int> v[1001];
		int start;
		int sum = 0;
		int arr[1001];
		
		memset(adj, 0, sizeof(adj));
		
		for(int i = 0; i<E; i++){
			int a,b,c;
			cin >> a >> b >> c;
			adj[a].push_back(make_pair(b,c));
			adj[b].push_back(make_pair(a,c));
		}
		
		
		for(int i = 0; i<N; i++){
			cin >> arr[i];
		}
		

		for(int i = 0; i<M; i++){
			cin >> start;
			v[i] = dijkstra(start);
		}
		
		
		for(int i = 0; i<N; i++){
			
		}
		
		cout << sum;
	}
}
