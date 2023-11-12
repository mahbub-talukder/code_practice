# if __name__ == '__main__':
# n = int(input())
# arr = sorted(map(int, input().split()))
# winner = arr[-1]
# score_without_winner = [i for i in arr if i != winner]
# runner_up  = score_without_winner[-1]
# print(runner_up)

"""problem 2"""
# records = []
# for item in range(int(input())):
#     name = input()
#     score = float(input())
#     records.append([name,score])

# records = sorted(records,key=lambda x : x[1]) 

# without_lowest =  [item for item in records if item[1] > records[0][1]] 

# second_lowest_names = sorted([item[0] for item in without_lowest if item[1] == without_lowest[0][1]])

# for name in second_lowest_names:
#     print(name)


# new_arr = [['a',20],['d',50],['c',50],['f',30],['b',90]]
# score_counts = {}
# for item in records:
#     score = item[1]
#     if score in score_counts:
#         score_counts[score].append(item)
#     else:
#         score_counts[score] = [item]

# duplicated_scores = sorted([sub_item[0] for items in score_counts.values() if len(items) > 1 for sub_item in items])
# for name in duplicated_scores:
#     print(name)


"""problem3: The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
 Print the average of the marks array for the student name provided, showing 2 places after the decimal."""

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

marks_array  = student_marks[query_name] if query_name in student_marks else None
if marks_array:
    avg = sum(marks_array)/len(marks_array)
    print("{:.f}".format(avg))
else:
    ValueError("query name is not correct")