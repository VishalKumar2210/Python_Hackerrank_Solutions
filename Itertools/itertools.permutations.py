from itertools import permutations

str1, int1 = input().split()

for i in sorted(permutations(str1, int(int1))):
    print(''.join(i))

# Steps Used in solving the problem -
# Step 1: First we imported the permutations from itertools.
# Step 2: then we have taken the input of str1 and int1.
# Step 3: In the third step, we used a for loop in our sorted permutations of str1 and int1.
# Step 4: then we used the join method to join our characters and printed them.
