import numpy
numpy.set_printoptions(sign=' ')
def arrays(arr):
    arr1 = numpy.array(arr, dtype = float)

    floor = numpy.floor(arr1)
    ceil = numpy.ceil(arr1)
    rint = numpy.rint(arr1)

    return floor, ceil, rint
arr = input().strip().split(' ')
floor, ceil, rint = arrays(arr)
print(floor)
print(ceil)
print(rint)