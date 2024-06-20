import re
t = int(input())
for _ in range(t):
    n = input()
    pattern = r'[+.-]?\d*\.\d+$'
    m = re.match(pattern, n)
    if m:
        print(True)
    else:
        print(False)