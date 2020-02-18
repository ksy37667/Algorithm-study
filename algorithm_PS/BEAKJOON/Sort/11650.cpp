#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(const pair<int,int> &a, const pair<int,int> &b){
	if(a.first < b.first){
		return true;
	}else if(a.first == b.first){
		return a.second < b.second;
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
