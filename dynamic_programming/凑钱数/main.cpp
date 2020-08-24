#include<iostream>
#include<vector>

using namespace std;

int min_num_coins(vector<int> &,int amount);

int main(){
    vector<int> coins={1,2,3,6,5,4,5,2,1,3,5};
    int amount=11;
    int res;
    res=min_num_coins(coins,amount);
    cout<<res<<endl;
    return 0;
}

int min_num_coins(vector<int>& coins,int amount){
vector<int> dp(amount+1,amount+1);
dp[0]=0;
for(int i=0;i<dp.size();i++){
    for(int coin:coins){
        if(i-coin<0) continue;
        dp[i]=min(dp[i],1+dp[i-coin]);

    }
}
return (dp[amount]==amount+1)? -1:dp[amount];
}