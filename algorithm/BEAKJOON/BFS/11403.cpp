#include <iostream>
#include <queue>

using namespace std;

int N;
int arr[100][100];

void bfs(){
	for(int i = 0; i<N; i++){
		queue<int> q;
		bool visited[N] = {};
		q.push(i);
		while(!q.empty()){
			int tmp = q.front();
			q.pop();
			for(int j = 0; j<N; j++){
				if(arr[tmp][j] == 1 && visited[j] != true){
					q.push(j);
					visited[j] = true;
					arr[i][j] = 1;
				}
			}
		}
	}
}

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N;
	
	for(int i = 0; i<N; i++){
		for(int j = 0; j<N; j++){
			cin >> arr[i][j]; 
		}
	}
	bfs();
	for(int i = 0; i<N; i++){
		for(int j = 0; j<N; j++){
			cout << arr[i][j] << " ";	
		}
		cout << "\n";
	}

}
