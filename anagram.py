def Anagram():
    Input1=input(" ")
    Input2=input(" ")
    i=0
    while i < len(Input1):
        if len(Input1) == len(Input2):
            if Input1[i] in Input2:
                print("YES")
                break
            else:
                print("NO")
                break
        i=i+1
Anagram()
    
