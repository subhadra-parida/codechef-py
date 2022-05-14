def SumOfDifference():
    n=int(input())
    m=int(input())
    i=0
    Sum1=0
    Sum2=0
    while i<=(m):
        if i%n==0:
            Sum1=Sum1+i
        else:
            Sum2=Sum2+i
        i=i+1
    return Sum2-Sum1
print(SumOfDifference())
            