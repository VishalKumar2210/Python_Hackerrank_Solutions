# Read main set
main_set = set(map(int, input().split()))

# Read number of other sets
n = int(input())

other_sets = [set(map(int, input().split())) for _ in range(n)]

# Check if main set is a strict superset of all other sets
print(all(main_set > other_set for other_set in other_sets))