def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



# Steps Used in solving the problem -
# Step 1: First we created a function. This function will take a number as input.
# Step 2: then, we created a variable.
# Step 3: then, we created a loop in the range 1 to num+1.
# Step 4: then, we changed our i in binary, octal, decimal, and hexadecimal.
# Step 5: At last we printed our all variables