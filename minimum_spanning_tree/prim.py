
#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_A&lang=jp

import heapq

N=int(input())
root=[{} for i in range(N)]
for i in range(N):
    temp=list(map(int,input().split()))
    for j in range(N):
        if temp[j]!=-1:
            root[i][j]=temp[j]

def main():
    ans=0
    
    visited=[0]*N
    connection=0
    q=[[0,0]]
    heapq.heapify(q)
    
    while q:
        cost,node=heapq.heappop(q)
        if visited[node]:
            continue
        
        visited[node]=1
        ans+=cost
        connection+=1
        for k,v in root[node].items():
            heapq.heappush(q,[v,k])
        if connection==N:
            break
    
    return ans

print(main())


