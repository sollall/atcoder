# coding: utf-8
# Your code here!
MOD=998244353
fact = [1] * 200001
for i in range(1, 200001):
	fact[i] = fact[i-1] * i % MOD
 
def comb(n, r):
	return fact[n] * pow(fact[r], -1, MOD) * pow(fact[n-r], -1, MOD) % MOD

N,M,K=map(int,input().split())

edges=[{} for i in range(N)]
for _ in range(M):
    u,v=map(int,input().split())
    u-=1
    v-=1
    edges[u][v]=1
    edges[v][u]=1

odd=0
even=0
for i in range(N):
    if len(edges[i])%2==1:
        odd+=1
    else:
        even+=1

ans=0


for odd_num in range(K+1)[::2]:
    even_num=K-odd_num
    if odd_num<=odd and even_num<=even:
        ans+=comb(odd,odd_num)*comb(even,even_num)
        ans%=MOD
    
print(ans)

    