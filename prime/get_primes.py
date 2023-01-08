#Nまでの素数を列挙
def get_prime(N):

    prime=[i for i in range(N)]

    for n in range(2,N):
        if prime[n]==n:
            for i in range(n,N)[::n]:
                prime[i]=n

    prime=sorted(list(set(prime))[2:])

    return prime


#エラトステネスの篩
#こっちのほうが微妙に早い　pypyなら10**7くらいまでいける
def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes
