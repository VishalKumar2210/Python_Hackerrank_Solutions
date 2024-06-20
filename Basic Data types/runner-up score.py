if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = set(arr)
    arr2 = sorted(arr1)
    print(arr2[-2])


# Steps Used in solving the problem -
# Step 1: First n will take an integer type input of n scores.

# Step 2: then, arr will make a list of these n scores.

# Step 3: After this, we converted our list to set so, it will not store multiple same integers.

# Step 4: then, I sorted my list of scores.

# Step 5: In the last step I printed the second-last integer of my list. And, it is the runner-up score.