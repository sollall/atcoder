import heapq

def bfs(length,node):
    dis[node]=length

    for n_node in way[node]:
        if dis[n_node]==-1:
            heapq.heappush(q,[length+1,n_node])
    return 

N,K=map(int,input().split())

dis=[-1]*N
dis[0]=0
way=[[] for i in range(N)]

for _ in range(N-1):
    a,b=map(int,input().split())
    way[a-1].append(b-1)
    way[b-1].append(a-1)

print(way)
q=[[0,0]]
heapq.heapify(q)

while q:
    temp=heapq.heappop(q)
    print(temp)
    bfs(temp[0],temp[1])

dis.sort()
if K>len(dis):
    print(-1)
else:
    print(sum(dis[:K]))