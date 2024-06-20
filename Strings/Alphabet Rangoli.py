a = "abcdefghijklmnopqrstuvwxyz"


def print_rangoli(size):
    lines = []
    for row in range(size):
        print_ = "-".join(a[row:size])
        lines.append(print_[::-1] + print_[1:])
    width = len(lines[0])

    for row in range(size - 1, 0, -1):
        print(lines[row].center(width, '-'))

    for row in range(size):
        print(lines[row].center(width, '-'))
    # your code goes here


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Steps Used in solving the problem -
# Step 1: First we have created a string of all alphabets.
# Step 2: then, we created a function. This function will take size as input.
# Step 3: then, we created an empty list to store our output.
# Step 4: Inside our function, we created a for loop. It will loop within the range of size.
# Step 5: then, we have used a join function to add a hyphen between our string letters within the range of size.
# Step 6: then, we declared a width variable.
# Step 7: then, we created another for loop to print the lower part of the rangoli.
# Step 8: and, we used another loop to print the upper part of the rangoli.
