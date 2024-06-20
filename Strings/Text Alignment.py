thickness = int(input()) #This must be an odd number
c = 'H'
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):  print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

for i in range(thickness+1): print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

for i in range(thickness):  print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))




# Steps Used in solving the problem -
# Step 1: First we created a variable to take input.
# Step 2: then, we created a string H.
# Step 3: then, we created a first for loop to print the top cone, 
# a second loop to print top pillars, 
# a third loop to print middle belt, 
# fourth for loop to print bottom pillars, 
# and fifth for loop to print the bottom cone