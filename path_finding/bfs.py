#これは順序を渡す
#bfs本体
from collections import deque

q=deque()

def bfs(h,w,num):
    visited[h][w]=num
    
    if h>0:
        if S[h-1][w]=="." and visited[h-1][w]==-1:
            q.append([h-1,w,num+1])
    if h<H-1:
        if S[h+1][w]=="." and visited[h+1][w]==-1:
            q.append([h+1,w,num+1])
    if w>0:
        if S[h][w-1]=="." and visited[h][w-1]==-1:
            q.append([h,w-1,num+1])
    if w<W-1:
        if S[h][w+1]=="." and visited[h][w+1]==-1:
            q.append([h,w+1,num+1])
    return


def bfs(edges,start):
    n_node=len(edges)
    costs=[float("inf") for i in range(N)]
    
    queue=[[0,start]]
    
    while queue:
        cost,now=hq.heappop(queue)
        if costs[now]>cost:
            costs[now]=cost
            for nxt,n_cost in edges[now].items():
                hq.heappush(queue,[cost+n_cost,nxt])
 
    return costs[:]