from collections import deque

t = int(input())
for i in range(t):
    size = int(input())
    top = 2 ** 31
    d = deque(list(map(int, input().split())))
    for j in range(len(d)):
        if d[len(d) - 1] <= d[0] <= top:
            top = d.popleft()
        elif d[len(d) - 1] <= top:
            top = d.pop()
        else:
            print('No')
            break
    if len(d) == 0:
        print('Yes')
