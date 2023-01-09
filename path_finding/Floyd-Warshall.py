#ちょっとかえないといけないhttps://atcoder.jp/contests/abc208/tasks/abc208_d

#たぶんあってる
def warshall_Floyd(edges):
    n_node=len(edges)
    costs=[[float("inf") if i!=j else 0 for i in range(n_node)] for j in range(n_node)]
    
    for index,edge in enumerate(edges):
        for nxt,cost in edge.items():
            costs[index][nxt]=min(costs[index][nxt],cost)
        
    
    for k in range(n_node):
        for i in range(n_node):
            for j in range(n_node):
                costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])
    
    return costs[:]