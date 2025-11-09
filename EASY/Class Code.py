s = ''
for i in range(1,5001):
    s += str(i)   
#'1234567...'
x = int(input())
print(s[x-1])