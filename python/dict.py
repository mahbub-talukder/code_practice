# Numeric types
from collections import defaultdict


numeric_dict = {1: 'one', 1 : 5, 2.5: 'two point five'}

# String
string_dict = {'apple': 'fruit', 'banana': 'fruit'}

# Tuple
tuple_dict = {(1, 2): 'pair', ('a', 'b'): 'letters'}

# Boolean
boolean_dict = {True: 'true', False: 'false'}

# Frozenset
frozenset_dict = {frozenset([1, 2, 3]): 'frozen set'}

# Custom object
class CustomObject:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)
obj1 = CustomObject(42)
custom_object_dict = {obj1: 'custom object'}

print(numeric_dict)
print(string_dict)
print(tuple_dict)
print(boolean_dict)
print(frozenset_dict)
print(custom_object_dict)
print(custom_object_dict[obj1])

keys = list(numeric_dict.items())
print("keys-->", keys)

d = defaultdict(lambda:'key not found')
# d['amar'] = 5
# d['amar'].append("something")
print("d-->", d['amar'])
