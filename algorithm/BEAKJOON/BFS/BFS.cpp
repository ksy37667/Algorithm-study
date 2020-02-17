#include <iostream>
#include <queue>

using namespace std;

int dx[4] = {0,0,-1,1}; // »óÇÏÁÂ¿ì 
int dy[4] = {1,-1,0,0};

int N,M;

int map[1001][1001];
int cnt;

queue< pair<int,int> > q;


int bfs(){
	while(!q.empty()){
		
		for(int i = 0; i<4; i++){
			int rx = q.front().first + dx[i];
			int ry = q.front().second + dy[i];
			
			if(rx >= 0 && ry >= 0 && rx < N && ry < M){
				
				if(map[rx][ry] == 0){
					map[rx][ry] = map[q.front().first][q.front().second] + 1;
					q.push(make_pair(rx,ry));
					cnt = map[rx][ry];
				}
			}
		}
		q.pop();
	}
	
	for(int i = 0; i<N; i++){
		for(int j = 0; j<M; j++){
			if(map[i][j] == 0){
				return -1;
			}
		}
	}
	if(cnt == 0) return 0;
	return cnt-1;
}

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> M >> N;
	
	for(int i = 0; i<N; i++){
		for(int j = 0; j<M; j++){
			cin >> map[i][j];
			if(map[i][j] == 1){
				q.push(make_pair(i,j));
			}
		}
	}
	cout << bfs();
	
	return 0;
}
