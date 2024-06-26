# Read input
n = int(input())
A = set(map(int, input().split()))
num_operations = int(input())

# Perform each operation on set A
for _ in range(num_operations):
    operation, _ = input().split()
    other_set = set(map(int, input().split()))
    if operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "update":
        A.update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)

# Output the sum of elements in set A
print(sum(A))