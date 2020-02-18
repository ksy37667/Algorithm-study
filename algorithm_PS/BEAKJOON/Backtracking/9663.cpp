#include <iostream>
#include <cmath>

using namespace std;

int count = 0;
int N;
bool Queen1[20];
bool Queen2[20];
bool Queen3[20];


void func(int k){
	if(k == N){
		count++;
		return ;
	}
	
	for(int i = 0; i<N; i++){
		if(Queen1[i] || Queen2[k+i] || Queen3[k-i+N-1]) continue;
		Queen1[i] = 1;
		Queen2[k+i] = 1;
		Queen3[k-i+N-1] = 1;
		func(k+1);
		Queen1[i] = 0;
		Queen2[k+i] = 0;
		Queen3[k-i+N-1] = 0;
	}
}

int main(){
	ios::sync_with_stdio(0);
  	cin.tie(0);
	cin >> N;
	func(0);
	
	cout << count;	
}


