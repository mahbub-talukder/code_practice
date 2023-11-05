##Tuple##
# words = ("spam", "eggs", "sausages")
# print(words[0])
# words[1] = "cheese"
#Tuples can be created without the parentheses by just separating the values with commas.
# my_tuple = "one", "two", "three"
# print(my_tuple[0])

# #* Tuple Unpacking [A variable that is prefaced with an asterisk (*) takes all values from the collection that are left over from the other variables.]

# a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# print(b)
# print(c)
# print(d)
# a, b, c, d, *e, f, g = range(20)
# print(len(e))

# print("range(20)-->", set(range(5,20,3)))

# skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
# job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
# print(skills & job_skills)

# a = {1, 2, 3}
# b = {0, 3, 4, 5}
# print(a & b)

# nums = [55, 44, 33, 22]
# print(max(min(nums[:2]), abs(-42)))
# print("min(nums[:2])-->", nums[:-1])

"""Functional Programming 
Functional programming is a style of programming that (as the name suggests) is based around functions. 

A key part of functional programming is higher-order functions. Higher-order functions take other functions as arguments, or return them as results.
"""
# def test(func, arg):
#   return func(func(arg))

# def mult(x):
#   return x * x

# print(test(mult, 2))


# nums = [11, 22, 33, 44, 55]
# res = list(filter(lambda x: x%2==0, nums))
# print(res)

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))


# #recursion
# def is_even(x):
#   if x == 0:
#     return True
#   else:
#     return is_odd(x-1)

# def is_odd(x):
#   return not is_even(x)


# print(is_odd(17))
# print(is_even(23))

# def fib(x):
#   if x == 0 or x == 1:
#     return 1
#   else: 
#     return fib(x-1) + fib(x-2)
# print(fib(4))


def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)


nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print("nums-->", nums)
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))

