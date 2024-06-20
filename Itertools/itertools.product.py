from itertools import product

input_A = list(map(int, input().split()))
input_B = list(map(int, input().split()))

print(*list(product(input_A, input_B)))


# Steps Used in solving the problem -
# Step 1: First we imported the product from itertools.
# Step 2: then we have taken the input of two lists.
# Step 3: In the last step, we used the product method with our both inputs. then we converted our output into a list and printed it.
#
# Note - we have used asterisk to unpack our list.