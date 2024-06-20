def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    string = "".join(lst)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    

# Steps Used in solving the problem -
# Step 1: First we created an function. this function takes a string, a position, and a character as input.
# Step 2: then we converted our string into a list.
# Step 3: After this, we defined the specific position of our list as equal to a character.
# Step 4: then we used a join method and joined our converted string.
# Step 5: In the last step, we returned our string.