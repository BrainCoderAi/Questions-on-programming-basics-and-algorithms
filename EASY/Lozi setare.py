c = int(input())

x = c
counter = 1
while x > 0:
    for i in range(x//2):
        print(' ', end = '')
    for j in range(counter):
        print('*', end = '')
    for i in range(x//2):
        print(' ', end = '')
    # --------------------------------

    for i in range(x//2):
        print(' ', end = '')
    for j in range(counter):
        print('*', end = '')
    for i in range(x//2):
        print(' ', end = '')
    
    print()
    counter += 2
    x -= 2

x = 1
counter = c-2
while counter > 0:
    for i in range(x):
        print(' ', end='')
    for j in range(counter):
        print('*', end='')
    for i in range(x):
        print(' ', end='')
    # ------------------------------
    
    for i in range(x):
        print(' ', end='')
    for j in range(counter):
        print('*', end='')
    for i in range(x):
        print(' ', end='')
        
    print()
    counter -= 2
    x += 1