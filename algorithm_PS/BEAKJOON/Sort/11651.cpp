#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(const pair<int,int> &a, const pair<int,int> &b){
	if(a.second < b.second){
		return true;
	}else if(a.second == b.second){
		return a.first < b.first;
	}else{
		return false;
	}
}

int main(){
	int N;
	cin >> N;
	vector < pair<int,int> > arr;
	
	for(int i = 0;  i<N; i++){
		int x,y;
		cin >> x >> y;
		
		arr.push_back(make_pair(x,y));
	}

	
	sort(arr.begin(),arr.end(), compare);
	
	for(int i = 0; i<N; i++){
		cout << arr[i].first << " " << arr[i].second << "\n";
	}
}
