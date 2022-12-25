#groupにするならこう　順序ならnum+1を渡す

def dfs(h,w,num):
    visited[h][w]=num
    
    if h>0:
        if S[h-1][w]=="." and visited[h-1][w]==-1:
            dfs(h-1,w,num)
    if h<H-1:
        if S[h+1][w]=="." and visited[h+1][w]==-1:
            dfs(h+1,w,num)
    if w>0:
        if S[h][w-1]=="." and visited[h][w-1]==-1:
            dfs(h,w-1,num)
    if w<W-1:
        if S[h][w+1]=="." and visited[h][w+1]==-1:
            dfs(h,w+1,num)
    
    return