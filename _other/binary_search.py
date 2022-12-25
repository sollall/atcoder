#リストから探すとかだったら直さないと　頑張ってね

def binary_search(goal):
    high=10**9
    low=0
    
    while high-low>1:
        mid=(high+low)//2
        
        if goal<mid:
            high=mid
        else:
            low=mid
            
    return mid