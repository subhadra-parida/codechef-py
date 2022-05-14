t=int(input("Enter any testcase="))
i=0
while i<t:
    a=int(input("Enter any number="))
    b=int(input("Enter any number="))
    a1=int(input("Enter any number="))
    b1=int(input("Enter any number="))
    a2=int(input("Enter any number="))
    b2=int(input("Enter any number="))
    if (a==a1 and b==b1) or (b==a1 and a==b1):
        print('1')
    elif (a==a2 and b==b2) or (b==a2 and a==b2):
        print('2')
    else:
        print('0')
    i=i+1

