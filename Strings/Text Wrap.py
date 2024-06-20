import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# What Is Textwrap?
# Text wrap is a python module used to wrap and format plain text.

# Steps Used in solving the problem -
# Step 1: First we have imported textwrap.
# Step 2: then, we created a function that takes a string and returns it wrapped in lines of max_width characters.
# Step 3: in the final step we used the textwrap.fill function to wrap the given paragraph according to max_width.