#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	ios_base::sync_with_stdio(0);
	int T; 
	cin >> T;

	for(int test = 0; test < T; test++){
		vector<char> v1;
		vector<char> v2;
		
		string str;
		cin >> str;
		
		for(char c : str){
			if(c == '-'){
				if(v1.size() != 0){
					v1.erase(v1.end()-1);
				}
			}else if(c == '<'){
				if(v1.size() != 0){
					v2.push_back(v1.back());
					v1.erase(v1.end()-1);
				}
			}else if(c == '>'){
				if(v2.size() != 0){
					v1.push_back(v2.back());
					v2.erase(v2.end()-1);
				}
			}else{
				v1.push_back(c);
			}
		}
		
		for(int i = 0; i<v1.size(); i++){
			cout << v1[i];
		}
		
		reverse(v2.begin(), v2.end());
		
		for(int i = 0; i<v2.size(); i++){
			cout << v2[i];
		}
		
		cout << "\n";
	}
}
