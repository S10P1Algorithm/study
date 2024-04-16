#include <bitset>
#include <fstream>
#include <iostream>

using namespace std;
const int N = 152;
int n,k,arr[N],sum[N],score[N][N]; 
//score[i][j] : i번부터 j번까지 맞았을 경우의 점수
//if j>i : then score [j][i] = 0 
//100+200+ .... + 15000 < 1140000
bitset<1140000> DT[N];
void input(){
    ios::sync_with_stdio(false); cin.tie(0);
    cin>>n;
    for(int i=1;i<=n;i++)
        cin>>arr[i],sum[i]=sum[i-1]+arr[i];
    for(int i=1;i<=n;i++)
        for(int j=i;j<=n;j++)
            score[i][j]=score[i][j-1]+sum[j]-sum[i-1];
    cin>>k;
}
void solve(){
    if(k>score[1][n]){
        cout<<k;
        return;
    }
    DT[0].set(0);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i+1;j++){
        // j부터 i번째 문제까지 연속해서 맞았을 가능한 점수
        // j=i+1 이면 i번째 문제를 틀린 것. 
            if(j<=2)
                DT[i].set(score[j][i]);
            else
                DT[i] |= (DT[j-2]<<score[j][i]);
        }
    }
    int ans=k;
    while(DT[n].test(ans)) ans++;
    cout<<ans;
}
int main(){
    input();
    solve();
    return 0;
}