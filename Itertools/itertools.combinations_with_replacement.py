# Enter your code here. Read input from STDIN. Print output to STDOUT

# from itertools import combinations_with_replacement

# str1, int1 = input().split()

# for i in combinations_with_replacement(str1, int(int1)):
#     print(''.join(i))

from itertools import combinations_with_replacement

io = input().split()
char = sorted(io[0])
N = int(io[1])

for i in combinations_with_replacement(char, N):
    print(''.join(i))
