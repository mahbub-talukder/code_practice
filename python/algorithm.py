#!/bin/python3

import math
import os
import random
import re
import sys



# def compareTriplets(a, b):
#     # Write your code here
#     result = [0,0]
#     for index in range(len(a)):
#         if a[index] > b[index]:
#             result[0] += 1
#         elif a[index] < b[index]:
#             result[1] += 1
#     return result

# if __name__ == '__main__':


#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     print(result)


"""problem2: 
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr  is shown below:
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal 1+5+9 = 15 . The right to left diagonal 3+5+9 = 15 . Their absolute difference is . |15-17| = 2
"""

# def diagonalDifference(arr):
#     # Write your code here
#     n= len(arr)
#     rtl_sum = 0
#     ltr_sum = 0
#     for i in range(n):
#         rtl_sum+= arr[i][i]
#         ltr_sum+= arr[i][n-i-1]
#     abs_diff = abs(rtl_sum-ltr_sum)
#     return abs_diff

# arr = [[1, 2, 3],
#     [4, 5, 6],
#     [9, 8, 9]]

# result = diagonalDifference(arr)


"""problem3:
We define a magic square to be an n x n matrix of distinct positive Integers from 1 to n² where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.
You will be given a 3 x 3 matrix s of integers in the inclusive range [1,9]. We can convert any digit a to any other digit b in the range [1,9] at cost of lab. Given s, convert it into a magic square at minimal cost. Print this cost on a new line.
Note: The resulting magic square must contain distinct integers in the inclusive range [1,9].

Example
$s=[[5, 3, 4], [1, 5, 8], [6, 4, 2]]
The matrix looks like this:
5 3 4
1 5 8
6 4 2
We can convert it to the following magic square:
8 3 4
1 5 9
6 7 2
This took three replacements at a cost of |5-8| + |8- 9| + |4-7| = 7

Function Description
Complete the formingMagicSquare function in the editor below.

formingMagicSquare has the following parameter(s):
    int s[3][3]: a 3 x 3 array of integers
Returns
    int: the minimal total cost of converting the input square to a magic square

"""
# def generate_magic_square(n):
#     magic_square = [[0] * n for _ in range(n)]

#     i, j = 0, n // 2
#     num = 1

#     while num <= n * n:
#         magic_square[i][j] = num
#         num += 1
#         i -= 1
#         j += 1

#         if i == -1 and j == n:
#             i, j = 1, n - 1
#         elif i == -1:
#             i = n - 1
#         elif j == n:
#             j = 0
#         elif magic_square[i][j] != 0:
#             i += 2
#             j -= 1

#     return magic_square

# # Example usage:
# n = 3
# magic_square = generate_magic_square(n)
# for row in magic_square:
#     print(row)






"""problem 4:
Given an array of integers, find the longest subarray where the absolute difference between any two elements is 
less than or equal to 1.

Example
a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
There are two subarrays meeting the criterion: [1, 1, 2, 2] and [4, 4, 5, 5, 5]. The maximum length subarray has 5 elements.

Function Description
Complete the pickingNumbers function in the editor below.
pickingNumbers has the following parameter(s):
int a[n]: an array of integers
Returns
int: the length of the longest subarray that meets the criterion
"""

def pickingNumbers(a):
    # Create a dictionary to store the count of each element in the array
    element_count = {}
    
    # Count the occurrences of each element in the array
    for num in a:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
            
    
    # Initialize the maximum length of subarray
    max_length = 0
    max_subarray = []
    # Iterate through each unique element in the array
    for num in element_count:
        # Check the length of subarray with current element and its adjacent element
        current_length = element_count[num] + element_count.get(num + 1, 0)

        # Update the maximum length if the current length is greater
        if current_length > max_length:
            max_length = current_length
            max_subarray = [num] * element_count[num] + [num + 1] * element_count.get(num + 1, 0)
    
    return max_length

# Example usage:
# a = [5,5,5,5,5,5,5,5,5,5,5,5,7,7,7,7,7,7]
# result = pickingNumbers(a)
# print(result)

#again practice 

# def pickingNumbers(a):
#     frequency_count = {}

#     for item in a:
#         frequency_count[item] = frequency_count.get(item,0) + 1

#     max_length = 0
#     long_subarray = []
#     for item in frequency_count:
#         subarray_length =  frequency_count[item] + frequency_count.get(item+1,0) # where 0-1 absolute diff between two item of the array

#         if subarray_length > max_length:
#             max_length = subarray_length
#             long_subarray = ([item] * frequency_count[item]) + ([item+1] * frequency_count.get(item+1,0)) 

#     return max_length

# a = [1,5,5,3,4,9,3,3,4,5,9,7]
# result = pickingNumbers(a)
# print(result)

"""problem 5
An arcade game player wants to climb to the top of the leaderboard and track their ranking. 
The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
"""

# def climbingLeaderboard(ranked, player):
#     # Write your code here
#     ranked=set(ranked)
#     player_rank = []
#     for score  in player:
#         new_list = list(ranked)
#         new_list.append(score)
#         new_list.sort(reverse=True)
#         player_rank.append(new_list.index(score)+1)

        
#     return player_rank

            

        
# ranked = [100,100,50,40,40,20,10]
# player_score = [5,20,50,120]
# result = climbingLeaderboard(ranked, player_score)
# print("result-->", result)

#efficient solution

# def search(arr, low, high, key):
#     mid = (low + high) // 2
    
#     if low > high:
#         return low
#     if arr[mid] == key:
#         return mid
#     if arr[mid] < key:
#         return search(arr, low, mid-1, key)
#     return search(arr, mid+1, high, key)

# def climbingLeaderboard(ranked, player):
#     # Write your code here
#     ranks = [1] * (len(ranked) + 1)
#     rank = 1
    
#     for i in range(1, len(ranked)):
#         if ranked[i - 1] != ranked[i]:
#             rank += 1
        
#         ranks[i] = rank
    
#     ranks[-1] = ranks[-2] + 1
    
#     r = []

#     for score in player:
#         i = search(ranked, 0, len(ranked) - 1, score)
#         r.append(ranks[i])
    
#     return r

# ranked = [100,100,50,40,40,20,10]
# player_score = [5,20,50,120]
# result = climbingLeaderboard(ranked, player_score)
# print("result-->", result)


"""problem 6

"""


# def plusMinus(arr):
#     # Write your code here
#     total_len =  len(arr)
#     positive =  [item for item in arr if item > 0]
#     negetive =  [item for item in arr if item < 0]
#     zero =  [item for item in arr if item == 0]
#     pos_ratio =  "{:6f}".format(len(positive)/total_len)
#     print(pos_ratio)
#     neg_ratio =  "{:6f}".format(len(negetive)/total_len)
#     print(neg_ratio)
#     zero_ratio =  "{:6f}".format(len(zero)/total_len)
#     print(zero_ratio)

# arr = [-4, 3, -9, 0, 4, 1]

# plusMinus(arr)


n = int(input())
integer_list = map(int, input().split())

# Create a tuple
t = tuple(integer_list)

# Print the hash value of the tuple
print(hash(t))
