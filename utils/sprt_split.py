#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B

m,q=map(int,input().split())

unit=1000

A=[0]*m
sum_log=[0]*(-(-m//unit))


for _ in range(q):
    c,x,y=map(int,input().split())

    
    if c==0:
        x-=1
        A[x]+=y
        idx=x//unit
        sum_log[idx]=sum(A[unit*idx:unit*(idx+1)])
        
    else:
        x-=1
        y-=1
        left=x//unit
        right=y//unit
        
        #print(left,right)
        
        ans=0

        if left!=right:
            for i in range(left+1,right):
                ans+=sum_log[i]
            ans+=sum(A[x:(left+1)*unit])
            ans+=sum(A[right*unit:y+1])
        else:
            ans+=sum(A[x:y+1])
        
        print(ans)
        
    
    