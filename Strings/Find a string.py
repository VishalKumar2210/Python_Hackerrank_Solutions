def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        if string[i:len(string)].startswith(sub_string):
            total += 1
    return total


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# Steps Used in solving the problem -
# Step 1: First we created an function. this function takes a string & sub_string as input.
# Step 2: then, we defined a variable to store the total.
# Step 3: then, we created a for loop that iterates in the range of length of the string.
# Step 4: Inside for loop, we had given an if condition to check if a string starts with a substring.
# Step 5: In the last step, we returned our string.
