# coding: utf-8
# Your code here!
#ABC293-E

A,K,M=map(int,input().split())

    
def my_fib(A,N,M):
    
    RA = RD = 1; RB = RC = 0
    XA=A
    XB=1
    XC=0
    XD=1
    #log=[(XA,XB,XC,XD)]
    
    while N:
        if N & 1:
            # R <- RX
            RA, RB, RC, RD = (RA*XA + RB*XC) % M, (RA*XB + RB*XD) % M, (RC*XA + RD*XC) % M, (RC*XB + RD*XD) % M
        XA, XB, XC, XD = (XA**2 + XB*XC) % M, XB*(XA + XD) % M, XC*(XA + XD) % M, (XB*XC + XD**2) % M
        N>>=1
        
        #log.append((XA,XB,XC,XD))
    
    
    return RA,RB,RC,RD


ans=my_fib(A,K,M)

print(ans[1])