r=1
for i in range(4):
    for j in range(4-i):
        print(" ",end=" ")
    for k in range(r):
        print("*",end=" ")
        k=k+1
    print() 
    r=r+2
    i=i+1       