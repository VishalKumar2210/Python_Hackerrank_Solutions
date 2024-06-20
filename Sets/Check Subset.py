# Read number of test cases
t = int(input())

for _ in range(t):
    # Read set A
    n = int(input())
    set_a = set(input().split())

    # Read set B
    m = int(input())
    set_b = set(input().split())
    
    # Check if set A is a subset of set B
    print(set_a.issubset(set_b))