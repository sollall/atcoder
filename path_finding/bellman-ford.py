#https://atcoder.jp/contests/abc061/tasks/abc061_d

def bellman_ford(start,edges):
    V=len(edges)
    all_cost=[float("inf")]*V
    all_cost[start]=0
    
    is_roop=False
    for i in range(V*2+1):
        for now,edge in enumerate(edges):
            for nxt,cost in edge.items():
                if all_cost[nxt]>all_cost[now]+cost:
                    all_cost[nxt]=all_cost[now]+cost
                    if nxt==V-1 and i==V*2:
                        is_roop=True
    
    return is_roop,all_cost[:]