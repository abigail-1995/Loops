for i in range(6):
    for j in range(6-i):
        print(" ",end=" ")
    for c in range (i):
        print(i,end=" ")
    for k in range (2,0,1):
        print(" ",end=" ")
    for l in range (1,i):
        print(i,end=" ")
    print()