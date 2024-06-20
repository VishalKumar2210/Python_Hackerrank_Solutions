import numpy

N, M = map(int, input().split())

array = numpy.array([input().split() for i in range(N)], int)

print(numpy.prod(numpy.sum(array, axis = 0), axis = None))

# Hint first calculate the product and then the sum,

# if you do other way you cannot complete the other two test cases.(I g