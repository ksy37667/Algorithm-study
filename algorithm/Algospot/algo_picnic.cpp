#include <iostream>
#include <string.h>

using namespace std;

bool check[10][10];
int N,M,cnt;

void func(bool taken[10]){
	int trigger = -1;
	for(int i = 0; i<N; i++){
		if(!taken[i]){
			trigger = i;
			break;
		}
	}
	if(M == 0){
		return ;
	}
	
	if(trigger == -1){
		cnt++;
		return ;	
	}
	
	for(int i = trigger+1; i<N; ++i){
		if(!taken[i] && check[trigger][i]){
			taken[trigger] = taken[i] = true;
			func(taken);
			taken[trigger] = taken[i] = false;
		}
	}
	
	return ;
}

int main(void)

{
        int test;
        
        cin >> test;

        for (int i = 0; i < test; i++)
        {
         	cnt = 0;
         	bool taken[10] = {0,};
	       	cin >> N >> M;
   	        memset(check, false, sizeof(check));
  	        for (int j = 0; j < M; j++)
  	        {
            	int x, y;
                cin >> x >> y;
                check[x][y] = check[y][x] = true;
           	}
           	func(taken);
           	cout << cnt << "\n";
        }

        return 0;

}
