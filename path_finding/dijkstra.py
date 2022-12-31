import heapq as hq

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