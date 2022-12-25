V,E,r=map(int,input().split())

edges=[]
for _ in range(E):
    s,t,d=map(int,input().split())
    edges.append([s,t,d])


cost=[float("inf")]*V
cost[r]=0

for i in range(V+1):
    judge=False
    
    for edge in edges:
        s,t,d=edge
        if cost[t]>cost[s]+d:
            cost[t]=cost[s]+d
            judge=True
    if i==V and judge:
        print("NEGATIVE CYCLE")
        exit()
        
        
for c in cost:
    if c==float("inf"):
        print("INF")
    else:
        print(c)
