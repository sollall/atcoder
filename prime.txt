#素数を列挙
N=10**5+1

prime=[i for i in range(N)]

for n in range(2,N):
    if prime[n]==n:
        for i in range(n,N)[::n]:
            prime[i]=n

prime=sorted(list(set(prime))[2:])

print(prime)