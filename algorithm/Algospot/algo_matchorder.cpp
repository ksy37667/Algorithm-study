#include <iostream>
#include <vector>
#include <set>

using namespace std;
vector<int> kor;
vector<int> rus;

int N = 0;

int greedy(){
	int cnt = 0;
	multiset<int> rating(kor.begin(), kor.end());
	
	for(int i = 0; i<N; i++){
		if(*rating.rbegin() < rus[i]){
			rating.erase(rating.begin());
		}else{
			rating.erase(rating.lower_bound(rus[i]));
			cnt++;
		}
	}
	
	return cnt;
}

int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	int T;
	cin >> T;
	
	for(int test = 0; test<T; test++){
		
		cin >> N;
		
		int sc = 0;
		for(int i = 0; i<N; i++){
			cin >> sc;
			rus.push_back(sc);
		}
		for(int i = 0; i<N; i++){
			cin >> sc;
			kor.push_back(sc);
		}
		
		cout << greedy() << endl;
		
		kor.clear();
		rus.clear();
	}

}
