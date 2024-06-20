import numpy

a = numpy.array(input().split() , int)
b = numpy.array(input().split() , int)
# print("---------------------------")
print(numpy.inner(a, b))
# print("---------------------------")
print(numpy.outer(a, b))