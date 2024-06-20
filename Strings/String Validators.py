if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s) )
    print(any(i.isalpha() for i in s) )
    print(any(i.isdigit() for i in s) )
    print(any(i.islower() for i in s) )
    print(any(i.isupper() for i in s) )


# Steps Used in solving the problem -
# Step 1: First s will take input.
# Step 2: then we used “any” to check whether the given conditions are true or false. 
# In this, we also used five different functions to check different properties with a for loop.