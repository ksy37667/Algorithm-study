#include <iostream>

using namespace std;

int N,M;

void func(int *arr, int *ck, int k){
	if(k == M){
		for(int i = 0; i<M; i++){
			cout << arr[i]+1 << " ";
		}
		
		cout << "\n";
		return ;
	}
	int st = 0;
	if(st < arr[st+1]) st = arr[k-1];
	
	for(int i = st; i<N; i++){
		if(!ck[i]){
			ck[i] = 1;
			arr[k] = i;
			func(arr,ck,k+1);
			ck[i] = 0;
		}
	}
}

int main(){
	ios::sync_with_stdio(0);
  	cin.tie(0);
  	
  	cin >> N >> M;
  	
	int arr[M] = {};
	int ck[N] = {};
	
	func(arr,ck,0);
		
}
