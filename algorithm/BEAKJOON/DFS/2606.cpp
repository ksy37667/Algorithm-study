#include <iostream>
#include <vector>

using namespace std;

int N,M;
vector<vector<int> > virus;
int visited[101] = {};
int cnt = 0;

void dfs(int x){
	visited[x] = true;
	for(int i = 0; i<virus[x].size(); i++){
		int y = virus[x][i];
		if(visited[y] == false){
			dfs(y);
			cnt++;
		}
	}
	return;
}

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M;
	
	virus.resize(N+1);
	
	for(int i = 0; i<M; i++){
		int x,y;
		cin >> x >> y;
		
		virus[x].push_back(y);
		virus[y].push_back(x);
	}

	dfs(1);
	
	
	cout << cnt;
}
