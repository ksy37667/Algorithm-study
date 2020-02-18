#include <iostream>
#include <algorithm>

using namespace std;

int N,M;
int t_arr[8];

void func(int* arr, bool* ck, int k){
	if(k == M){
		for(int i = 0; i<M; i++){
			cout << arr[i] << " ";
		}
		cout << "\n";
		return ;
	}
	
	
	for(int i = 0; i<N; i++){
		if(k == 0){
			arr[k] = t_arr[i];
			ck[i] = 1;
			func(arr,ck,k+1);
			ck[i] = 0;
		}else{
			if(arr[k-1] <= t_arr[i]){
				arr[k] = t_arr[i];
				ck[i] = 1;
				func(arr,ck,k+1);
				ck[i] = 0;
			}	
		}

	}
}

int main(){
	cin >> N >> M;
	
	int arr[M] = {};
	bool ck[N] = {};
	
	for(int i = 0; i<N; i++){
		cin >> t_arr[i];
	}
	sort(t_arr, t_arr+N);
	

	
	func(arr,ck,0);
}
