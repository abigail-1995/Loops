for i in range(1,6):
    for j in range(1,6):
        if j==i or i+j==6 or i==1 or j==3 or i==5:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()           