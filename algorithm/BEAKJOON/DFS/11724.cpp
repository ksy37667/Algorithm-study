#include <iostream>
#include <vector>


using namespace std;

int N,M;

vector<int> map[1001];
bool visit[1001];


int dfs(int start){
	visit[start] = true;
	
	for(int i = 0; i<map[start].size(); i++){
		int next = map[start][i];
		
		if(!visit[next]) dfs(next);
	}
}

int main(){
	cin >> N >> M;
	for(int i = 0; i<M; i++){
		int u,v;
		cin >> u >> v;
		
		map[u].push_back(v);
		map[v].push_back(u);
	}
	int cnt = 0;
	
	for(int i = 1; i<=N; i++){
		if(!visit[i]){
			dfs(i);
			cnt++;
		}
	}
	
	cout << cnt;
	
	return 0;
}
