#Q1.What are the five key conceot of oops?

'''1.Encapsulation:Bundling the data and methods that operate on the 
  data into a single unit or class.

2.Abstraction:Hiding the implementation details of a class & only showing the essential features
  to the user.

3.Inheritance:A mechanism by which one class (the child or subclass) inherits the properties and 
  behaviour from another class.

4.Polymorphism:The ability to use a single interface to represent different data types or classes.

5.Composition:Building complex objects by combining objects of other classes.'''

#Q2.Write a python class for a car with attributes for make model and year.include a method 
# to display the cars information.

'''class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print(f"cars information:{self.model} {self.make} {self.year}")    
mycar=car("Toyota","camry",2020)
mycar.display_info()'''


#Q3.Explain the difference between instance method and class method,provide an example of each.

'''Instance Methods:

Definition: Instance methods are the most common type of methods in a class. They operate on
            an instance of the class and can access and modify the instance’s attributes.
Definition: They take self as the first parameter, which refers to the instance of the class.

Example:

class Dog:
    def __init__(self, name):
        self.name = name
#instance method
    def bark(self):
        return f"{self.name} says Woof!"

# Usage
my_dog = Dog("Buddy")
print(my_dog.bark())  # Output: Buddy says Woof!

Class Methods:

Definition: Class methods operate on the class itself rather than on instances of the class.
            They can access class attributes and methods but not instance attributes.
Definition: They take cls as the first parameter and are marked with the @classmethod decorator.

Example:

class Dog:
    count = 0  # Class attribute to keep track of dog instances

    def __init__(self, name):
        self.name = name
        Dog.count += 1  # Increment count whenever a new instance is created

    @classmethod
    def total_dogs(cls):
        return cls.count

# Usage
dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(Dog.total_dogs())  # Output: 2

Summary

Instance methods work with individual object instances and have access to their attributes.
Class methods work with the class as a whole and have access to class-level attributes.'''

#Q4.How does python implement method overloading?Give an Example.

'''Python does not support method overloading in the same way that languages like Java or C++ do.
 In those languages, you can define multiple methods with the same name but different parameter
 lists. In Python, however, you can only define one method with a specific name in a class.

 Instead, Python achieves similar functionality through the following approaches:

 Default Arguments: You can provide default values for parameters in a method,
 allowing you to call the method with varying numbers of arguments.

class Example:
    def method(self, a, b=0):
        return a + b

obj = Example()
print(obj.method(5))     
print(obj.method(5, 10))  '''

#Q5.What are the three type of access modifier in python?how are they denoted.

'''In Python, there are three types of access modifiers that control the visibility of 
class attributes and methods:

Public: Attributes and methods are accessible from outside the class. By default, all 
        class members are public.

class MyClass:
    def __init__(self):
        self.public_attr = "I am public"
    
    def public_method(self):
        return "This is a public method"

obj = MyClass()
print(obj.public_attr)  # Accessible, output:I am public

Protected: Attributes and methods are intended to be accessible only within the class and 
           its subclasses. They are denoted by a single underscore prefix (_).

class MyClass:
    def __init__(self):
        self._protected_attr = "I am protected"
    
    def _protected_method(self):
        return "This is a protected method"

obj = MyClass()
print(obj._protected_attr)  # Accessible, but discouraged
#output:I am protected

Private: Attributes and methods are intended to be accessible only within the class itself.
         They are denoted by a double underscore prefix (__). This invokes name mangling, making 
         it harder to access from outside the class.

class MyClass:
    def __init__(self):
        self.__private_attr = "I am private"
    
    def __private_method(self):
        return "This is a private method"

obj = MyClass()
# print(obj.__private_attr)  # Raises AttributeError'''

#Q6.Describe the five types of inheritance in python .provide a simple example of 
# multiple inheritance.

'''Inheritance is defined as the mechanism of inheriting the properties of the base class to
the child class.
      
Types of Inheritance:

Single Inheritance: Single inheritance enables a derived class to inherit properties from
                    a single parent class, thus enabling code reusability and the addition of new 
                    features to existing code.

Multilevel Inheritance :In multilevel inheritance, features of the base class and the derived 
                        class are further inherited into the new derived class. This is similar to
                        a relationship representing a child and a grandfather. 

Hierarchical Inheritance: When more than one derived class are created from a single base this 
                          type of inheritance is called hierarchical inheritance.

Hybrid Inheritance: Inheritance consisting of multiple types of inheritance is called hybrid
                    inheritance.

Multiple Inheritance: When a class can be derived from more than one base class this type
                      of inheritance is called multiple inheritances. In multiple inheritances,
                      all the features of the base classes are inherited into the derived class. 


Example of multiple Inheritance:

#Base class1

class Parent1:
    def greet(self):
        return "Hello from Parent1!"

#Base class2

class Parent2:
    def greet(self):
        return "Hello from Parent2!"

#Derived class

class Child(Parent1, Parent2):
    def hello(self):
        return "Hello from Child!"

# Create an instance of Child
ch = Child()

# Call methods
print(ch.greet())  # Calls greet from Parent1
print(ch.hello())  # Calls hello from Child'''

#Q7.What is the Method resolution order(MRO)in python? how can you retrieve it programatically.


'''Method Resolution Order : In Python defines the order in which base classes are searched  
(MRO)                     when executing a method or accessing an attribute. This is
                          especially important in multiple inheritance scenarios, where a 
                          method might exist in more than one parent class.

How to Retrieve MRO Programmatically: You can retrieve the MRO of a class using two main methods:

Using the mro() method
Using the __mro__ attribute

Example:

Here's a simple example demonstrating both methods:

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# Retrieve MRO
print(D.mro())          # Using mro() method
print(D.__mro__)        #Using __mro__ attribute'''

#Q8.Create an abstract base class 'shape' with an abstract method "area()".then create two 
# subclasses "circle" and "rectangle" that implement the "area()" method.

'''from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print(f"Area of Circle: {circle.area():.2f}")
    print(f"Area of Rectangle: {rectangle.area()}")'''


#Q9.Demonstrate polymorphism by creating a function that can work with different shape objects
    #to calculate and print their areas.
    
'''Polymorphism allows us to use the same interface for different data types. In the context of 
shapes, we can define a base class Shape and then create derived classes like Circle, Rectangle,
and Triangle. Each derived class will implement a method to calculate its area.

    
import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Derived class for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Function to calculate and print areas
def print_area(shape):
    print(f"The area is: {shape.area()}")

# Creating instances of each shape
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 5)

# Using the print_area function with different shapes
print_area(circle)
print_area(rectangle)
print_area(triangle)'''


#Q10.Implement Encapsulation in a "BankAccount" class with private attribute for "balance"  and
     #"account_number". Include methods for deposit, withdrawal, and balance inquiry.


'''Example:

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self._account_number = account_number  # Private attribute
        self._balance = initial_balance          # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

# Example usage
account = BankAccount("123456789", 100)
account.deposit(50)
account.withdraw(30)
print(f"Current Balance: ${account.get_balance():.2f}")
print(f"Account Number: {account.get_account_number()}")'''

#Q11.Write a class that overrides the '__str__ and '__add__' magic methods. 
#    What will these methods allow you to do?

'''Example:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        #Return a string representation of the point.
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        #Add two points together.
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

# Example usage
p1 = Point(2, 3)
p2 = Point(4, 5)

# Using __str__ to print the point
print(p1)  # Output: Point(2, 3)
print(p2)  # Output: Point(4, 5)

# Using __add__ to add two points
p3 = p1 + p2
print(p3)  # Output: Point(6, 8)'''


#Q12.Create a Decorator that measures and prints the execution times of a function in simple way. 


'''import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timeit
def example_function(n):
    total = sum(range(n))
    return total

# Call the decorated function
result = example_function(1000000)
print(f"Result: {result}")'''


#Q13.Explain the concept of the Diamond Problem in multiple inheritance. How does python 
#    resolve it?


'''The Diamond Problem occurs in object-oriented programming languages that support multiple 
inheritance. It arises when a class inherits from two classes that both inherit from a common 
ancestor.

Python uses a technique called Method Resolution Order (MRO) to resolve this ambiguity.
The MRO defines the order in which classes are looked up when searching for a method or attribute.
Python employs the C3 linearization algorithm for this purpose.

Key Points of MRO:

C3 Linearization: This algorithm provides a consistent order for method resolution, 
ensuring that a class is only considered after its parents and in a left-to-right order. 
This prevents the diamond problem by giving precedence to the first class in the inheritance list.

Single Search Path: When you call a method on an instance of D, Python checks D, then B, then C, 
and finally A, following the MRO.

super() Function: The super() function can be used to access methods from parent classes in a way
that respects the MRO. It helps avoid direct references to the parent classes, allowing for more 
flexible and maintainable code.

Here is an simple example:

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()  # Outputs: Hello from B

# Check MRO
print(D.mro())'''


#Q14.Write a class method that keeps track of the number of a instance created from a class.

'''class InstanceCounter:
    count = 0  # Class variable to keep track of the number of instances

    def __init__(self):
        InstanceCounter.count += 1  # Increment count when an instance is created

    @classmethod
    def get_instance_count(cls):
        return cls.count  # Return the current instance count

# Example usage
if __name__ == "__main__":
    obj1 = InstanceCounter()
    obj2 = InstanceCounter()
    obj3 = InstanceCounter()

    print(f"Number of instances created: {InstanceCounter.get_instance_count()}")  # Outputs: 3'''


#Q15.Implement a static method in a class that checks if a given year is a leap year.


'''class YearChecker:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage
year = int(input("Enter a year you want to check:"))
print(f"{year} is a leap year: {YearChecker.is_leap_year(year)}")'''


