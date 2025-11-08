x, y = map(int, input().split())

lst = []
c = 1
while x != 0:
    lst.append(x%y)
    x = x//y

s = ''
a = ['A', 'B', 'C', 'D', 'E', 'F']
for i in range(len(lst)-1, -1,-1):
    if int(lst[i]) > 9:
        s += a[lst[i]%10]
    else:
        s += str(lst[i])

print(s)