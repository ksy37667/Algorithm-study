#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>

using namespace std;

int N,M;
int arr[50][50];

vector < pair <int, int> > home;
vector < pair <int, int> > chicken;

bool ck[13] = {};
int minimum = 9876543;
int dis = 9876543;

void func(int dept, int k){
	if(k == M){
		int sum;
		for(int i = 0; i<home.size(); i++){
			for(int j = 0; j<chicken.size(); j++){
				cout << abs(home[i].first - chicken[j].first) + abs(home[i].second - chicken[j].second) << " ";
				if(ck[j]) dis = min(dis, abs(home[i].first - chicken[j].first) + abs(home[i].second - chicken[j].second));	
			}
			sum += dis;

		}

		minimum = min(minimum,sum);	
		return ;
	}
	if(dept == chicken.size()) return;
	
	ck[dept] = 1;
	func(dept+1, k+1);
	ck[dept] = 0;
	func(dept+1, k);
}



int main(){
	
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    
    cin >> N >> M;
    for(int i = 0; i<N; i++){
    	for(int j = 0; j<N; j++){
    		cin >> arr[i][j];
    		if(arr[i][j] == 1){
    			home.push_back(make_pair(i,j));
			}else if(arr[i][j] == 2){
				chicken.push_back(make_pair(i,j));
			}
		}
	}
	func(0,0);
	
	cout << minimum;
}
