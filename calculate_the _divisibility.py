def Calculate():
    m=int(input())
    n=int(input())
    i=m
    sum=0
    while i<n:
        if (i%3==0 and i%5==0):
            sum=sum+i
        i+=1
    return sum
print(Calculate())