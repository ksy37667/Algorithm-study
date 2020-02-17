#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
const int INF = 987654321;

int N,M,X;

vector <pair <int, int> > adj[1001];


int dijkstra(int start, int end){
	vector<int> dist(N,INF);
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
	
	return dist[end];
}

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M >> X;
	
	N++;
	int arr[N] = {};
	
	for(int i = 0; i<M; i++){
		int a,b,c;
		cin >> a >> b >> c;
		adj[a].push_back(make_pair(b,c));
	}
	
	int go[N] = {};
	
	for(int i = 1; i<N; i++){
		go[i] = dijkstra(i,X) + dijkstra(X,i);
	}

	sort(go, go+N);
	
	cout << go[N-1];
}
