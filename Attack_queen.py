T=int(input())
for i in range(T):
    n=int(input("Enter any number="))
    x=int(input("Enter any number="))
    y=int(input("Enter any number="))
    a=2*n-2
    a+=min(x-1,n-y)
    a+=min(n-x,y-1)
    a+=min(x-1,y-1)
    a+=min(n-x,n-y)
    print(a)

