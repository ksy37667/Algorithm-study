#include <iostream>
#include <queue>

using namespace std;

queue< pair<int, int> > q;

int dx[8] = {0,0,1,-1,1,-1,1,-1};  
int dy[8] = {1,-1,0,0,1,-1,-1,1};
int map[51][51];


int bfs(int N, int M){
	int cnt = 0;
	
	for(int i = 0; i<M; i++){
		for(int j = 0; j<N; j++){
			
			if(map[i][j] == 1){
				map[i][j] == 0;
//				cout << i << j << endl;
				q.push(make_pair(i,j));
				while(!q.empty()){
					
					int x = q.front().first;
					int y = q.front().second;
					q.pop();
					
					for(int k = 0; k<8; k++){
						int rx = x + dx[k];
						int ry = y + dy[k];
						if(rx>=0 && ry >= 0 && rx < M && ry < N){
							if(map[rx][ry] == 1){
								map[rx][ry] = 0;
								q.push(make_pair(rx,ry));
							}
						}
					}
				}
				cnt++;
			}
		}
	}
	return cnt;
}


int main(){
	int a = 1;
	int b = 1;
	int w,h;
	while(1){
		cin >> w >> h;
		if(w==0 && h == 0) break;
		
		for(int i = 0; i<h; i++){
			for(int j = 0; j<w; j++){
				cin >> map[i][j];
			}
		}
		cout << bfs(w,h) << "\n";
		
	}
}
