row=int(input("enter num"))
for i in range(1,row+1):
    for j in range(i,row):
        print(end=" ")
    for c in range(1,i+1):
        print("*",end=" ")
    print( )       
for i in range(row,0,-1):
    for j in range(i,row+1):
        print(end=" ") 
    for c in range(1,i):
        print("*",end=" ")   
    print( )        