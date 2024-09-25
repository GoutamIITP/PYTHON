def squarefloor(n):
    if (n == 0 or n == 1):
        return n
    
    l = 1
    h = n // 2
    ans = 0
    while l <= h:
        mid = (l + h) // 2
        if (mid * mid == n):
            return mid
        
        if mid * mid < n:
            l = mid + 1
            ans = mid
        else:
            h = mid - 1
    return(ans)            

x = 5       
print(squarefloor(x))