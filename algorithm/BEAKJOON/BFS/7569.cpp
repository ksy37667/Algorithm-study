#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int arr[100][100][100] = {};
vector<pair<pair<int,int>,int> > save;
int N, M, H;

int dx[6] = {1,-1,0,0,0,0};
int dy[6] = {0,0,1,-1,0,0};
int dz[6] = {0,0,0,0,1,-1};
int cnt = 0;


int bfs(){
	queue<pair<pair<int,int>,int> > q;
	for(int T = 0; T<save.size(); T++){
		q.push(make_pair(make_pair(save[T].first.first, save[T].first.second),save[T].second));
	}
		
	
	while(!q.empty()){
		int x = q.front().first.first;
		int y = q.front().first.second;
		int z = q.front().second;
		
		q.pop();
		
		for(int i = 0; i<6; i++){
			int rx = x+dx[i];
			int ry = y+dy[i];
			int rz = z+dz[i];
			
			if(rx >= 0 && ry >= 0 && rz >= 0 && rx< H && ry < M && rz < N){
				if(arr[rx][ry][rz] == 0){
					arr[rx][ry][rz] = arr[x][y][z] + 1;
					q.push(make_pair(make_pair(rx,ry),rz));
					cnt = arr[rx][ry][rz];
				}else if(arr[rx][ry][rz] == -1 || arr[rx][ry][rz] == 1) continue;
			}
		}
	}
	if(cnt == 0){
		return cnt;
	}else{
		for(int i = 0; i<H; i++){
			for(int j = 0; j<M; j++){
				for(int k = 0; k < N; k++){
					if(arr[i][j][k] == 0){
						return cnt = -1;
					}
				}
			}
		}
	}
	return cnt-1;
}

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M >> H;
	
	for(int i = 0; i<H; i++){
		for(int j = 0; j<M; j++){
			for(int k = 0; k<N; k++){
				cin >> arr[i][j][k];
				if(arr[i][j][k] == 1){
					save.push_back(make_pair(make_pair(i,j),k));
				}
			}
		}
	}

	cout << bfs();
}
