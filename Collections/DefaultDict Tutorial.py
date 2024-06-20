from collections import defaultdict

input_n, input_m = map(int, input().split())
d = defaultdict(list)
for i in range(input_n):
    ans1 = input()
    d[ans1].append(i + 1)
for j in range(input_m):
    ans2 = input()
    if ans2 in d:
        print(*d[ans2])
    else:
        print(-1)

# Steps Used in solving the problem -
# Step 1: First we imported defaultdict from collections.
# Step 2: then we have taken the input of input_n and input_m.
# Step 3: then we defined defaultdict as d.
# Step 4: In the fourth line, we create a for loop in the range of input_n.
# Step 5: Inside for loop, we have taken input and appended it into d.
# Step 6: then we created another for loop in the range of input_m.
# Step 7: Inside for loop, we have taken input. Then we used an if condition to check if ans2 is in d
# then print the index value of ans2 else print -1
