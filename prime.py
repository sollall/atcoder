#素数を列挙
def get_prime(N):

    prime=[i for i in range(N)]

    for n in range(2,N):
        if prime[n]==n:
            for i in range(n,N)[::n]:
                prime[i]=n

    prime=sorted(list(set(prime))[2:])

    return prime