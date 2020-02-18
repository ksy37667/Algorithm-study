#include <iostream>

using namespace std;

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int a,b,c;
	c = 0;
	
	for(int i = 0; i<4; i++){
		cin >> a >> b;
		c = max(c,c+b-a);
	}
	
	cout << c;
}
