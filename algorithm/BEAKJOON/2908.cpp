#include <iostream>
#include <algorithm>

using namespace std;


int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	string str1,str2;
	
	cin >> str1 >> str2;
	
	reverse(str1.begin(), str1.end());
	reverse(str2.begin(), str2.end());
	
	if(atoi(str1.c_str()) < atoi(str2.c_str())){
		cout << atoi(str2.c_str());
	}else{
		cout << atoi(str1.c_str());
	}
	
	return 0;
}
