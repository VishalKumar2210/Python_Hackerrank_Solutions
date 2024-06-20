import numpy

X, Y, Z = map(int, input().split())
array = numpy.array([input().split() for i in range(X+Y)], int)

print(array)