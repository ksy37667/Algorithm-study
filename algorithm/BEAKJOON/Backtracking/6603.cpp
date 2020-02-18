#include <iostream>
#include <algorithm>

using namespace std;

int N;
int t_arr[13];

void func(int *arr, bool *ck, int k){
	if(k == 6){
		for(int i = 0; i<6 ;i++){
			cout << arr[i] << " ";
		}
		cout << "\n";
		return ;
	}
	
	for(int i = 0; i<N; i++){
		if(k != 0){
			if(!ck[i] && arr[k-1] < t_arr[i]){
				ck[i] = 1;
				arr[k] = t_arr[i];
				func(arr,ck,k+1);
				ck[i] = 0;
			}
		}else{
			ck[i] = 1;
			arr[k] = t_arr[i];
			func(arr,ck,k+1);
			ck[i] = 0;
		}

	}
}


int main(){
	
	while(1){
		int arr[6];
		bool ck[13];
		cin >> N;
		
		if(N == 0) break;
		
		
		for(int i = 0; i<N; i++){
			cin >> t_arr[i];
		}
		
		sort(t_arr,t_arr+N);
		
		func(arr,ck,0);
		cout << "\n";	
	}
}
