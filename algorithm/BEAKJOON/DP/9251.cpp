#include <cstdio>
#include <algorithm>
#include <cstring>
int cache[1001][1001];
char input[1001],compare[1000];
int LCS(){
    int n = strlen(compare), m = strlen(input);
    memset(cache,0,sizeof(cache));
    for(int i=1;i<=n;i++){
        for(int j=1; j<=m;j++){
            if(compare[i-1] == input[j-1]){
                cache[i][j] = cache[i-1][j-1] +1;
                }
            else{
                cache[i][j] = std::max(cache[i-1][j], cache[i][j-1]);
            }
        }
    }
    return cache[n][m];
}
int main(){
    scanf("%s %s",input,compare);
    printf("%d\n",LCS());
}
