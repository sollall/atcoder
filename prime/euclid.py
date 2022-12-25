#最小公約数を求める math.gcdでよいのでは

def euclid(a,b):
    return a if b==0 else euclid(b,a%b)


print(euclid(15,7))