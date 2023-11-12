
"""problem 1"""
# import numpy
# numpy.set_printoptions(legacy='1.13')
# n,m =  map(int,input().split(" "))

# print (numpy.eye(n, m, k = 0) ) 

"""problem solving"""

# s = set()
# s.update('hello', 'how', 'are', 'you?')
# print(len(s))

"""problem 6
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

A number is called a smart number if it has an odd number of factors. Given some numbers, find whether they are smart numbers or not.

Debug the given function is_smart_number to correctly check if a given number is a smart number.

Note: You can modify only one line in the given code and you cannot add or remove any new lines.

To restore the original code, click on the icon to the right of the language selector.


input:
4
1
2
7
169
output:
YES
NO
NO
YES

"""

import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val == val:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")


