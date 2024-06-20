for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(int(a//b))
    except Exception as e:
        print("Error Code:", e)

# Steps Used in solving the problem -
# Step 1: First we created a for loop in the range of integer input.
# Step 2: In the second line, we used the try method.
# Inside try we have taken the input of a and b. Then we printed the division of a and b.
# Step 3: At last we used except to handle exceptions
# If there is any error occurred during compiling then the error will get printed and our code will work continuously.