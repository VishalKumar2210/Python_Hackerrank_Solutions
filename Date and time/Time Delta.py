import math
import os
import random
import re
import sys
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    format_ = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, format_)
    t2 = datetime.strptime(t2, format_)
    return str(int(abs((t1 - t2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# Steps Used in solving the problem -
# Step 1:  First we imported DateTime.
# Step 2: then we created a string to add the format of date and time.
# Step 3: After this, we created two variables to store our inputs in our described format. Here we have used strptime function to return a string representation of our inputs.
# Step 4: At last we have returned the absolute difference of our inputs in seconds.
