#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false); cin.tie(0);
	long long N;
	long long sum = 0;
	cin >> N;
	
	long long dist[N-1];
	long long price[N];
	
	for(int i = 0; i<N-1; i++){
		cin >> dist[i];
	}
	
	for(int i = 0; i<N; i++){
		cin >> price[i];
	}
	
	long long cnt = 0;
	
	for(int i = 0; i<N-1; i++){
		if(i == 0){
			sum += price[0] * dist[0];
		}else{
			if(price[cnt] <= price[i]){
				sum += price[cnt]*dist[i];
			}else{
				cnt = i;
				sum += price[i]*dist[i]; 
			}
		}
	}
	
	cout << sum;
}
