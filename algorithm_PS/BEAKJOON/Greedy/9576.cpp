#include <iostream>
#include <algorithm>

using namespace std;

bool cmp(pair<int,int> a, pair<int,int> b){
	if(a.second == b.second){
		return a.first > b.first;
	}
	return a.second < b.second;
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0);
	int T;
	cin >> T;
	
	for(int test = 0; test<T; test++){
		int N, M, cnt = 0;

		cin >> N >> M;
		pair<int,int> student[M];
		bool book[N+1] = {};
		
		for(int i = 0; i<M; i++){
			cin >> student[i].first >> student[i].second;
		}
		
		sort(student,student+M, cmp);
		
		for(int i = 0; i<M; i++){
			for(int j = student[i].first; j<=student[i].second; j++){
				if(book[j] == 0){
					book[j] = true;
					cnt++;
					break;
				}
			}
		}
		cout << cnt << "\n";
	}
}
