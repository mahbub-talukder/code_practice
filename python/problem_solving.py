
import math
import os
import random
import re
import sys




#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        if i%3 == 0 and i%5==0:
            print("FizzBuzz")
        elif i%3 == 0 and i%5 !=0:
            print("Fizz")
        elif i%5 == 0 and i%3 !=0:
            
            print("Buzz")
        else:
            print(i)

"""problem 2 :
find the median of a list
"""
import statistics 

#method 1:
def findMedian(arr:list):
    mid =  len(arr)//2
    print("mid-->", mid)
    arr.sort()
    print("arr-->", arr)
    median =  (arr[mid] + arr[~mid]) / 2
    print("arr[mid]-->", arr[mid])
    print("arr[~mid]-->", arr[~mid])
    print("median-->", median)
arr = [6,7,9,12]
findMedian(arr)

def findMedian2(arr:list):
    mid =  len(arr)//2
    arr.sort()
    if len(arr)%2==0:
         median =  (arr[mid] + arr[~mid]) / 2
    else:
         median =  arr[mid]

    print(median)
    
arr = [6,7,9,12]
findMedian2(arr)

def findMedian3(arr:list):
    median = statistics.median(arr)

    print(median)
    
arr = [6,7,9,12]
findMedian2(arr)


"""problem4:
Given an array of integers, where all elements but one occur twice, find the unique element.

Example
a = [1,2,4,2,1]

The unique element is 4.



"""
def lonelyinteger(a):
    # Write your code here
    frequency_count = {}
    for key in a:
        frequency_count[key] = frequency_count.get(key,0)+1
    
    for key in frequency_count:
        if frequency_count[key] == 1:
            return  key


a = [1,2,4,2,1]
lonelyinteger(a)
print("lonelyinteger-->", lonelyinteger(a))