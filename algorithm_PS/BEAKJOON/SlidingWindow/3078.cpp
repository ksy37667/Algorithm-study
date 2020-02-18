#include <iostream>
#include <queue>

using namespace std;

int main(){
	queue<int> q[21];
	int N, K;
	string str;
	
	long cnt = 0;
	
	cin >> N >> K;
	
	for(int i = 0; i<N; i++){
		cin >> str;
		
		if(!q[str.size()].empty()){
			while(i - q[str.size()].front() > K){
				q[str.size()].pop();
				if(q[str.size()].empty()){
					break;
				}
			}
			cnt += q[str.size()].size();
		}else{
			q[str.size()].push(i);
		}
	}	
	cout << cnt;
}

