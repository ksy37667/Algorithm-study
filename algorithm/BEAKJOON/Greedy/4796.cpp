#include <iostream>

using namespace std;



int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int L,P,V;
	int a = 1;
	
	while(1){
		cin >> L >> P >> V;
		if(L == 0 && P == 0 && V == 0) break;
		else{
			int option = (V%P) > L ? L : V%P;
        	int result = (V / P)*L + option;
        	cout << "Case " << a++ << ": " << result << "\n";
		}
	}
}

