# coding: utf-8
# Your code here!

N=int(input())
S=list(input())
X=input()

dp=[[False]*7 for i in range(N+1)]
dp[N][0]=True


for i in range(N)[::-1]:
    for j in range(7):
        if X[i]=="T":
            dp[i][j]=False
            dp[i][j]|=dp[i+1][(j*10+int(S[i]))%7]
            dp[i][j]|=dp[i+1][(j*10)%7]
            
        else:
            dp[i][j]=True
            dp[i][j]&=dp[i+1][(j*10+int(S[i]))%7]
            dp[i][j]&=dp[i+1][(j*10)%7]


if dp[0][0]:
    print("Takahashi")
else:
    print("Aoki")