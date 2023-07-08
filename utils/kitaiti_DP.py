# ABD280E - Critical Hit

MOD=998244353

N,P=map(int,input().split())

dp=[0]*(N+1)
dp[1]=1

inv100 = pow(100, MOD-2, MOD)

for i in range(2,N+1):
    dp[i]=dp[i-2]*P*inv100+dp[i-1]*(100-P)*inv100+1
    dp[i]%=MOD

print(dp[-1])
    
    