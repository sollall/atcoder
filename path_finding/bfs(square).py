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

#初期値
H,W=map(int,input().split())

Ch,Cw=map(int,input().split())
Dh,Dw=map(int,input().split())

S=[]
for _ in range(H):
    S.append(list(input()))

visited=[[-1 for i in range(W)] for j in range(H)]

#実働
for i in range(H):
    for j in range(W):
        if S[i][j]=="." and visited[i][j]==-1:
            q.append([i,j,0])
        while q:
            h,w,num=q.popleft()
            bfs(h,w,num)

print(visited)