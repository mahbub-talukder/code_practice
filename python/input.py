# def check_polynomial(x:int, k:int, polynomial:str):
#     # Evaluate the polynomial at the given x
#     result = eval(polynomial.replace('x', str(x)))

#     # Check if the result equals k
#     return result == k

# # Read input values
# x, k = map(int, input().split())
# polynomial = input()

# # Check and print the result
# print(check_polynomial(x, k, polynomial))

"""problem 2"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n])


# Initialize an empty list to store the combinations
result = []

# Use nested loops to generate combinations
for a in range(x + 1):
    print("loop a-->",a)
    for b in range(y + 1):
        print("loop b-->",b)

        for c in range(z + 1):
            print("loop c-->",c)

            # Check the condition and append to the result list
            if a + b + c != n:
                result.append([a, b, c])

# Print the final list of combinations
# print(result)



