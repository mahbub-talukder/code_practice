import getpass
from oop_tutorial import MyClass
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pprint = pprint.PrettyPrinter(indent=4).pprint

class A:
    cls_variable = 10  # class variable
    name = 'Mahbub'

    # def __new__(cls):
    #     cls.cls_variable = 20
    #     return cls
    # def __new__(cls, *args, **kwargs):
    #     # print("Creating a new instance")
    #     instance = super().__new__(cls)
    #     return instance

    def __init__(self) -> None:
        self.x = 10  # instance variable
        self.y = 15  # instance variable
        self.z = 10  # instance variable
        self.m = 15  # instance variable
        self.n = 10  # instance variable
        self.p = 15  # instance variable

    def show(self):  # instance method
        print("1")
        print("3")
        # print("x-->", self.x, 'y--->', self.y)

    @classmethod
    def example_cls_method(cls):  # class method
        # print('x--->',self.x) # can't access instance variable #!AttributeError: type object 'A' has no attribute 'x'
        # can't access instance variable
        print('class variable--->', cls.cls_variable)

    @staticmethod
    def extra_work(other):  # static method
        print('other any value--->', other)  # any value from outside

    def __str__(self):
        return str(self.name)

class B(A):

    # @classmethod
    def show(self):  # instance method
        print("1")
        print("2")
        print("3")
        


class D(A):

    # @classmethod
    # def show(self):  # instance method
    pass

        



if __name__ == "__main__":

    
    a_obj =  A()
    print("a_obj", a_obj.show())
    b_obj =  B()
    # print("b_obj", B.show())
    print("b_obj", b_obj.show())

    d_obj = D()
    d_obj.show()
  
    # Output: my_module
