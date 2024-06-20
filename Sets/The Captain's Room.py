# Read input
k = int(input())
room_numbers = list(map(int, input().split()))

# Compute the sum of all room numbers
total_sum = sum(room_numbers)

# Compute the sum of unique room numbers
unique_sum = sum(set(room_numbers))

# Calculate the Captain's room number using the formula
captain_room = (unique_sum * k - total_sum) // (k - 1)

print(captain_room)