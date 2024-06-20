import re

n = int(input())
for i in range(0, n):
    try:
        input_ = input()
        a = (re.compile(input_))
        print(bool(a))
    except re.error:
        print('False')


# import re
# n = int(input())
# for _ in range(n):
#     try:
#         s = input()
#         p = re.compile(s)
#         print("True")
#     except re.error:
#         print("False")

# Steps used in solving the problem -
# Step 1: First we imported re.
# Step 2: then, we have taken the input of n.
# Step 3: After this, we created a for loop in the range of 0 to (n).
# Step 4: Inside for loop, we used the try method and took input.
# Step 5: then, we used re.compile method with our input.
# Step 6: After this, we printed our answer as a boolean.
# Step 7: at last we used the expect method to handle exceptions
# if any exception occurs it will print ("False").
