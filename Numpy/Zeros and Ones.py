import numpy


def arrays(arr):
    arr1 = numpy.array(arr, dtype=int)
    arr2 = numpy.zeros(arr1, dtype=int)
    arr3 = numpy.ones(arr1, dtype=int)
    return arr2, arr3


arr = input().strip().split(' ')
arr2, arr3 = arrays(arr)

print(arr2)
print(arr3)
