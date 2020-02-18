#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	int N,M;
	int tmp1, num;
	vector <int> arr1;

	
	cin >> N;
	
	for(int i = 0; i<N; i++){
		cin >> tmp1;
		arr1.push_back(tmp1);
	}
	sort(arr1.begin(),arr1.end());
	
	cin >> M;
	
	for(int i = 0; i<M; i++){
		cin >> num;
		
		cout << upper_bound(arr1.begin(),arr1.end(),num) - lower_bound(arr1.begin(),arr1.end(), num) << " ";
	}

}
