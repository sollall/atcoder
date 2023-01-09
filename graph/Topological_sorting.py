from collections import deque

def topological_sort(edges):
    N=len(edges)
    deg=[0]*N
    for v,_ in enumerate(edges):
        deg[v]+=1
    
    ans=list(v for v in range(N) if deg[v] == 0)
    deq=deque(ans)

    while deq:
        v = deq.popleft()
        for t in g[v]:
            deg[t] -= 1
            if deg[t] == 0:
                deq.append(t)
                ans.append(t)

    return ans