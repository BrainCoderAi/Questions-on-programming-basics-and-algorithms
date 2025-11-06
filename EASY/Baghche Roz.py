x, y = map(int, input().split())
lst = []
for i in range(y):
    lst.append(input())

counter = 0
for j in range(x):
    for i in range(y):
        if lst[i][j] == 'W':
            counter += 1
    if counter % 2 == 0:
        print('B', end='')
    else :
        print('F', end='')
    counter = 0