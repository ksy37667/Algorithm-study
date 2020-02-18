#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool cmp (pair<int, string> u, pair<int, string> v)
{
    return u.first < v.first;
}


int main(){
	ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int N;
	cin >> N;
	vector< pair <int, string> > v;
	
	for(int i = 0; i<N; i++){
		int a;
		string b;
		cin >> a >> b;
		v.push_back(make_pair(a,b));
	}
	
	stable_sort(v.begin(), v.end(), cmp);
	
	for(int i = 0; i<N; i++){
		cout << v[i].first << " " << v[i].second << "\n";
	}
	
	return 0;
}
