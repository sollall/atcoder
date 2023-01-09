class RollingHash:
    def __init__(self,s,base,mod):
        self.mod=mod
        
        N=len(s)
        self.pw=[1]*(N+1)
        self.h=[0]*(N+1)
        
        for n in range(N):
            self.h[n+1]=(self.h[n]*base+ord(s[n]))%self.mod
        for n in range(N):
            self.pw[n+1]=self.pw[n]*base%self.mod
            
    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod
        