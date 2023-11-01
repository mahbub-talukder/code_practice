from typing import Any


class Person:

    def __init__(self,name:int,dob:float,height)->None:
        self.name = name
        self.dob = dob
        self.height = height


    def get_summery(self):
       return f"name : {self.name}, dob :  {self.dob}, height: {self.height}ft"


    def __str__(self):
        return f"name : {self.name}, dob :  {self.dob}, height: {self.height}ft"
        




person1 =  Person('Mahbub','1997-10-14',5.2)
# print(person1)


class BankAccount:
   def __init__(self, account_number, balance):
      self.__account_number = account_number
      self.__balance = balance
    
   def _display_balance(self):
      print("Balance:", self.__balance,"ACC",self.__account_number)

# b = BankAccount(1234567890, 5000)
# b._display_balance() 

class Loan(BankAccount):

    def __init__(self, loan_date, amount):
        self.loan_date =  loan_date
        self.amount =  amount

        super().__init__('asdfasdf',968)
    def loan_summer(self):
        print("loan_date--->",self.loan_date,'loan_amount-->',self.amount)
    
# l =  Loan('2023-10-25',1000)

# l._display_balance()


class Deposit(Loan):
    def __init__(self, loan_date, amount):
        super().__init__(loan_date, amount)
        pass
    
    def show(self):
        print("Deposit summary")

    def __str__(self) -> str:
        return "deposit class print"
    
dep =  Deposit('2023-10-15',500)
# print(dir(dep))
if __name__ == "__main__":
    dep._display_balance()


class MyClass:
    """This is my class 
    """
    def __init__(self):
        self.attr_field = "Hello"
        self.another_field = "Hello"

    def __delattr__(self, name):
        print(f"Deleting attr_field '{name}'")
        super().__delattr__(name)

    def show_name(self):
        return self.attr_field
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        print("__value", __value)
        print("__name", __name)
        
        super().__setattr__(__name,__value)

    

# # Create an instance of MyClass
# obj = MyClass()

# # Access and print the attr_field
# # print(obj.attr_field)  # Output: Hello

# # Delete the attr_field using del
# del obj.attr_field

# print(obj.__doc__)

# print('=================\n',dir(obj),'\n')
# Attempting to access the attr_field after deletion will raise an AttributeError
# print(obj.attr_field)  # Uncommenting this line will result in AttributeError
