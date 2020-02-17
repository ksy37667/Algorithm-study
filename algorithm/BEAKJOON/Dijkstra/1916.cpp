#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N, M;
int src, des;
const int INF = 987654321;

vector <pair <int, int> > adj[1001];

vector<int> dijkstra(int src){
	
	vector<int> dist(N, INF);
	dist[src] = 0;
	
	priority_queue<pair<int,int>, vector<pair<int,int> >, greater<pair<int,int> > > pq;
	pq.push(make_pair(0,src));
	
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
				pq.push(make_pair(nextDist, there));
			}
		}
	}
	return dist;
}


int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M;
	
	N++;
	
	for(int i = 0; i<M; i++){
		int a,b,c;
		cin >> a >> b >> c;
		adj[a].push_back(make_pair(b,c));
	}
	cin >> src >> des ;
	
	vector<int> result = dijkstra(src);
	
	cout << result[des] << endl;
}
