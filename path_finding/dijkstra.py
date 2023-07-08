import heapq as hq
from collections import deque

def dijkstra(edges,start):
    n_node=len(edges)
    costs=[float("inf") for i in range(n_node)]
    
    queue=[[0,start]]
    
    while queue:
        cost,now=hq.heappop(queue)
        if costs[now]>cost:
            costs[now]=cost
            for nxt,n_cost in edges[now].items():
                hq.heappush(queue,[cost+n_cost,nxt])
 
    return costs[:]

#計算量O((V+E)logV
#移動コストが0かnの二択なら01bfsができるけど計算量はO(V+E)になるくらい
#01はdequeにして0なら先頭、nなら後ろに入れる

def bfs01(edges,start):
    n_node=len(edges)
    costs=[float("inf") for i in range(n_node)]
    
    queue=deque([[0,start]])
    
    while queue:
        cost,now=queue.popleft()
        if costs[now]>cost:
            costs[now]=cost
            for nxt,n_cost in edges[now].items():
                if n_cost>0:
                    queue.append([cost+n_cost,nxt])
                else:
                    queue.appendleft([cost+n_cost,nxt])
 
    return costs[:]