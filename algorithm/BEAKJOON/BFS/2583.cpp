#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int M,N,K;
int arr[100][100] = {};

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
int width[100] = {};
int cnt = 0;

void bfs(){
	queue< pair<int,int> > q;
	for(int i = 0; i<N; i++){
		for(int j = 0; j<M; j++){
			if(arr[i][j] == 0){
				arr[i][j] = 1;
				q.push(make_pair(i,j));
				while(!q.empty()){
					int x = q.front().first;
					int y = q.front().second;
					q.pop();
					width[cnt]++;
					for(int k = 0; k<4; k++){
						int rx = x+dx[k];
						int ry = y+dy[k];
						if(rx >= 0 && ry >= 0 && rx <N && ry <M){
							if(arr[rx][ry] == 0){
								arr[rx][ry] = 1;
								q.push(make_pair(rx,ry));
							}
						}
					}
				}
				cnt++;
			}
		}
	}
}

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M >> K;
	int x1,y1,x2,y2;
	for(int i = 0; i<K; i++){
		cin >> x1 >> y1 >> x2 >> y2;
		for(int j = y1; j<y2; j++){
			for(int k = x1; k<x2; k++){
				arr[j][k] = 1;
			}
		}
	}
	bfs();
	
	sort(width,width+cnt);
	cout << cnt << "\n";
	for(int i = 0; i<cnt; i++){
		cout << width[i] << " ";
	}
	
	return 0;
}
