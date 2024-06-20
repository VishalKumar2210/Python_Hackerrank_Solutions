n, m = map(int,input().split())
for i in range(n//2):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))
print('WELCOME'.center(m,'-'))
for i in reversed(range(n//2)):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))


# Steps Used in solving the problem -
# Step 1: First we have taken the input of n & m.
# Step 2: then, we created a for loop to print the first half part.
# Step 3: then, we printed the welcome line in the center.
# Step 4: in last, we created another for loop to print the last half part.