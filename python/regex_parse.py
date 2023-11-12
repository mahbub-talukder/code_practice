"""problem1:
Neo has a complex matrix script. The matrix script is a  X  grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

Capture.JPG

To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

"""

import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s=""
for i in range(m):# loop on column
    for j in range(n): # loop on row
        s+=matrix[j][i]
pattern=r"(?<=[a-zA-Z0-9])[\s!@#$%&]+(?=[a-zA-Z0-9])"
s=re.sub(pattern, " ", s)
print(s)


"""problem 2:
A valid postal code P  have to fullfil both below requirements:

1. P must be a number in the range from 100000 to 999999  inclusive.
2. P must not contain more than one alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.
Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:

regex_integer_in_range should match only integers range from  100000 to 999999 inclusive

regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.

Both these regular expressions will be used by the provided code template to check if the input string P is a valid postal code using the following expression:

(bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)



code template : 

`regex_integer_in_range = r"_________"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"_________"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
`
"""


regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
"""regex_integer_in_range:

^[1-9]: Ensures the first digit is between 1 and 9.
[0-9]{5}$: Matches exactly 5 digits after the first digit.
This ensures that the postal code is a number in the range from 100000 to 999999 inclusive."""

regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.
"""regex_alternating_repetitive_digit_pair:

(\d): Captures a digit.
(?=\d\1): Uses a positive lookahead to assert that the next digit is the same as the captured digit.
This will find alternating repetitive digit pairs"""


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)