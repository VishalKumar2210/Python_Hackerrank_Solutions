from collections import namedtuple
input_ = int(input())
my_fields = input().split()
total_marks = 0
for _ in range(input_):
    students = namedtuple('my_student', my_fields)
    MARKS, CLASS, NAME, ID = input().split()
    my_student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(my_student.MARKS)
print((total_marks / input_))

#
# Steps Used in solving the problem -
# Step 1:  First we imported namedtuple from collections.
# Step 2: then we created input for input_ and my_fields. And we also created a variable to store total marks.
# Step 3: After this, we created a for loop in range of out input_.
# Step 4: then we created namedtuple with my_student as key and my_fields as value.
# Step 5: then we created input for MARKS, CLASS, NAME, and ID. and, we have also stored our input in students.
# Step 6: In last we divided the total marks by input and printed it