#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N , cnt = 0;
char arr[9] = {};
bool ck[10] = {};
int t_arr[10] = {};

vector<int> v[362880];

void func(int k, int p){
	if(k == N+1){
		for(int i = 0; i<N+1; i++){
			v[cnt].push_back(t_arr[i]);
		}
		cnt++;
		return ;
	}
	
	for(int i = 0; i<10; i++){
		if(!ck[i]){
			if(k == 0){
				ck[i] = 1;
				t_arr[k] = i;
				func(k+1,p);
				ck[i] = 0;
			}else{
				if(arr[p] == '>'){
					if(t_arr[k-1] > i){
						ck[i] = 1;
						t_arr[k] = i;
						func(k+1,p+1);
						ck[i] = 0;
					}
				}else{
					if(t_arr[k-1] < i){
						ck[i] = 1;
						t_arr[k] = i;
						func(k+1,p+1);
						ck[i] = 0;
					}
				}
			}
		}
	}
	return ;
}

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N;
	for(int i = 0; i<N; i++){
		cin >> arr[i];
	}
	
	func(0,0);
	
	for(int i = 0; i<N+1; i++){
		cout << v[cnt-1][i];
	}
	
	cout << "\n";
	
	for(int i = 0; i<N+1; i++){
		cout << v[0][i];
	}
}


