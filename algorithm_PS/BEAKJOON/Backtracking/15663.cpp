#include <iostream>
#include <algorithm>

using namespace std;

int N,M;

int t_arr[8], cnt[8], num[8] = {};
int arr[8];

void count(){
	int count = 1;
	int st = 0;
	int tmp = t_arr[0];
	
	
	for(int i= 1; i<N; i++){
		if(tmp == t_arr[i]){
			count++;
		}else{
			cnt[st] = count;
			num[st] = tmp;
			count = 1;
			tmp = t_arr[i];
			st++;
		}
	}
	
	cnt[st] = count;
	num[st] = tmp;
	N = st;
}

void func(int k){
	if(k == M){
		for(int i = 0; i<M; i++){
			cout << arr[i] << " ";
		}
		cout << "\n";
		return ;
	}
	
	for(int i = 0; i<=N; i++){
		if(k != 0){
			if(cnt[i] && arr[k-1] <= num[i]){
				cnt[i] -= 1;
				arr[k] = num[i];
				func(k+1);
				cnt[i] +=1;
			}
		}else{
			cnt[i] -= 1;
			arr[k] = num[i];
			func(k+1);
			cnt[i] +=1;
		}
	}
}

int main(){
	ios::sync_with_stdio(0);
  	cin.tie(0);
	cin >> N >> M;
	
	
	for(int i = 0; i<N; i++){
		cin >> t_arr[i];
	}
	
	sort(t_arr, t_arr+N);
	count();
	func(0);
}


