n=int(input("enter num"))
a=1
for i in range(n+1):
    for j in range(i+1):
        print(a,end=" ")
    print()
    a=a+2    