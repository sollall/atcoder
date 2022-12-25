#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0189

while True:
    n=int(input())
    
    if n:
        cost=[[float("inf") for i in range(10)] for j in range(10)]
        d=[[float("inf") for i in range(10)] for j in range(10)]
        MAX=0
        for _ in range(n):
            a,b,c=map(int,input().split())
            cost[a][b]=min(c,cost[a][b])
            cost[b][a]=min(c,cost[b][a])
            MAX=max(MAX,a,b)
        
        #経路の点が一番上のイテレータ
        for k in range(10):
            for s in range(10):
                for t in range(10):
                    cost[s][t]=min(cost[s][k]+cost[k][t],cost[s][t])
        
        ans_node=-1
        ans_score=float("inf")
        for i in range(MAX+1):
            c=cost[i][:MAX+1]
            if ans_score>sum(c)-c[i]:
                ans_score=sum(c)-c[i]
                ans_node=i
        print(ans_node,ans_score)
    else:
        break
    
