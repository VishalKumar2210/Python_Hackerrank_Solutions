if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(
        list([i,j,k] 
               for i in range(x+1) 
               for j in range(y+1) 
               for k in range(z+1)  
               if i+j+k !=n)
               )


# Steps Used in solving the problem -
# Step 1: here x, y, z, and n will take integer type input.
# Step 2: then I used a print function to print my list.
# Step 3: inside a print function, I have used list Comprehension in which [i,j,k] is my output. 
# After this, I used 3 for loops for the values of i,j & k and after this, I used an if condition.