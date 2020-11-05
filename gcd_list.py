#リストの最小公倍数を返す

import math 

def gcd_list(lis):
    temp=0
    for item in lis:
        temp=math.gcd(temp,item)
    
    return temp

print(gcd_list([3,6,9]))