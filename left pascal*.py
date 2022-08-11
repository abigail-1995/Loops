rows = int(input("Enter rows"))
for i in range(1, rows + 1):
    for l in range(i, rows):
        print(end = '  ')
    for m in range(1, i + 1):
        print('*', end = ' ')
    print()
for i in range(rows, 0, -1):
    for l in range(i, rows + 1):
        print(end = '  ')
    for m in range(1, i):
        print('*', end = ' ')
    print()
