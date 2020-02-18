#include <iostream>

using namespace std;

int main(){
	
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int N = 1000;
	int en;
	int cnt = 0;
	
	cin >> en;
	
	N = N-en;
	
	while(N != 0){
		if(N>=500){
			cnt += 1;
			N = N-500;
		}else if(N<500 && N>=100){
			cnt += N/100;
			N = N-100*(N/100);
		}else if(N<100 && N >=50){
			cnt += 1;
			N = N-50;
		}else if(N<50 && N >= 10){
			cnt += N/10;
			N = N-10*(N/10);
		}else if(N<10 && N >= 5){
			cnt += N/5;
			N = N-5;
		}else if(N<5 && N >= 1){
			cnt += N;
			N = 0;
		}
	}
	
	cout << cnt;
}

