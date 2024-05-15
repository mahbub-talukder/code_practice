import math
from unittest import TestCase 

case_obj = TestCase()
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def test_add():
   num = 25
   assert 78 == 75


def test_sub():
   num = 25
   assert 50-5 == 45

def test_square():
   num = 7
   assert (7*7) == 40

def test_equality():
    case_obj.skipTest("mon caiche")
    case_obj.assertEqual(10,11)