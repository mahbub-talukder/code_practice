from abc import ABC, abstractmethod

# Abstract class representing a Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class Circle that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265359 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159265359 * self.radius

# Concrete class Rectangle that inherits from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Usage of the Shape, Circle, and Rectangle classes
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    

    print(f"Circle Area: {circle.area()}")
    print(f"Circle Perimeter: {circle.perimeter()}")

    print(f"Rectangle Area: {rectangle.area()}")
    print(f"Rectangle Perimeter: {rectangle.perimeter()}")
