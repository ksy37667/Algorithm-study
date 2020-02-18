#include <iostream>
#include <algorithm>

using namespace std;


int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int N, money, st, end, sum = 0;
	cin >> N;
	int arr[N];
	
	for(int i = 0; i<N; i++){
		cin >> arr[i];
	}
	
	sort(arr,arr+N);
	
	cin >> money;
	st = 0;
	end = arr[N-1];
	int mid = (st + end) / 2;
	int result = 0;
	
	while(st <= end){
		sum = 0;
		for(int i = 0; i<N; i++){
			if(arr[i] <= mid){
				sum += arr[i];
			}else{
				sum += mid;
			}
		}
		
		if(sum <= money){
			st = mid+1;
		}else{
			end = mid-1;
		}
		mid = (st + end) / 2;
	}
	
	cout << mid;
}


