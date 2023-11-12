"""Problem solved"""
import numpy 
dimension =  list(map(int,input().split()))
if len(dimension) == 3:
    x,y,z=dimension
    print(numpy.zeros((x,y,z),dtype=numpy.int8))
    print(numpy.ones((x,y,z),dtype=numpy.int8))
elif len(dimension) == 2:
    x,y=dimension
    print(numpy.zeros((x,y),dtype=numpy.int8))
    print(numpy.ones((x,y),dtype=numpy.int8))
else:
    x=dimension
    print(numpy.zeros((x),dtype=numpy.int8))
    print(numpy.ones((x),dtype=numpy.int8))

"""Problem solution"""

# import numpy
# n,m =  map(int,input().split())
# A,B=[],[]
# for _ in range(n):
#     A.append(list(map(int,input().split())))
# for _ in range(n):
#     B.append(list(map(int,input().split())))


# a = numpy.array(A, int,ndmin=n)
# b = numpy.array(B, int,ndmin=n)

# print(a + b) 

# print(a - b) 

# print(a * b)

# print(a // b)  

# print(a % b)           

# print(a**b)  

"""problem 3"""

# import numpy
# numpy.set_printoptions(legacy='1.13')
# arr =  list(map(float,input().split()))
# my_array = numpy.array(arr)
# print(numpy.floor(my_array))
# print(numpy.ceil(my_array))
# print(numpy.rint(my_array))

"""problem 6"""
# import numpy
# n,m =  map(int,input().split())
# a = []
# for _ in range(n):
#     a.append(list(map(int,input().split())))

# my_array = numpy.array(a)

# sum = numpy.sum(my_array, axis = 0)
# print(numpy.prod(sum))