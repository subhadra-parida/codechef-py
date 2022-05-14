for _ in range(int(input())):
    n=int(input())
    l =int(input("Enter any number="))
    l.sort(reverse=True)
    c=0
    h=0
    if (n==1):
       h=l[0]
    
    for i in range(0,n-1):
        if (l[i]==l[i+1]):
            c+=1
        elif h<l[i]+c:
            h=l[i]+c
            c=0
    print(h)