stick=int(input("Enter any number="))
for i in range(stick):
    list1=int(input("Enter any number="))
    list1=map(int, input().split())
    list2=set(list1)
    if 0 in list2:
        print(len(list2)-1)
    else:
        print(len(list2))

