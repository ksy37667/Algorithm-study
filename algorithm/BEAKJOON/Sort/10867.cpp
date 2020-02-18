#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	int N,tmp;
	cin >> N;
	
	vector <int> arr;
	
	
	for(int i = 0; i<N; i++){
		cin >> tmp;
		arr.push_back(tmp);
	}
	
	sort(arr.begin(),arr.end());
	arr.erase(unique(arr.begin(),arr.end()),arr.end());
	
	for(int i = 0; i<arr.size(); i++){
		cout << arr[i] << " ";
	}
	
}
