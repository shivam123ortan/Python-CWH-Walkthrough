# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def sum(n):
    if (n<=1): 
        return n
    else:
        return n + sum(n-1)

k = 9
s = sum(k)    
print(s)