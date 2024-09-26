# #Create a class Animal with a method speak that prints "Animal speaks". Then create a subclass Dog that overrides the speak method to print "Dog barks". Instantiate both classes and call their speak methods.

# # class Animal:
# #     def speak(self):
# #         print("Animal speaks")

# # class Dog(Animal):
# #     def speak(self):
# #         print("Dog barks")

# # # Instantiate and call methods
# # animal = Animal()
# # animal.speak()

# # dog = Dog()
# # dog.speak()

# #Create two classes Bird and Flyable. Bird should have a method fly that prints "Bird flies", and Flyable should have a method fly that prints "Flyable flies". Create a subclass Eagle that inherits from both Bird and Flyable. Instantiate the Eagle class and call the fly method. Note how Python resolves the method to call.

# # class Bird:
# #     def fly(self):
# #         print("Bird flies")

# # class Flyable:
# #     def fly(self):
# #         print("Flyable flies")

# # class Eagle(Bird, Flyable):
# #     pass

# # # Instantiate and call methods
# # eagle = Eagle()
# # eagle.fly()




# ##Create a class Vehicle with an _init_ method that initializes make and model attributes. Then create a subclass Car that also initializes make, model, and year attributes, using super() to call the parent class's _init_ method.


# class Vehicle:
#     def _init_(self, make, model):
#         self.make = make
#         self.model = model

# class Car(Vehicle):
#     def _init_(self, make, model, year):
#         super()._init_(make, model)
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.make} {self.model}")

# # Instantiate and call methods
# car = Car("Toyota", "Corolla", 2020)
# car.display_info()



# ##Create a class Shape with a method area that returns 0. Then create subclasses Square and Circle that override the area method to compute the area of a square and a circle, respectively. Demonstrate the usage by creating instances of Square and Circle and calling their area methods.


# class Shape:
#     def area(self):
#         return 0

# class Square(Shape):
#     def _init_(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

# class Circle(Shape):
#     def _init_(self, radius):
#         self.radius = radius

#     def area(self):
#         import math
#         return math.pi * self.radius * self.radius

# # Instantiate and call methods
# square = Square(4)
# print(square.area())

# circle = Circle(3)
# print(circle.area())


# ##Create a base class Employee with attributes name and salary. Create two subclasses Manager and Developer that inherit from Employee and add a method to print the role of the employee. Instantiate the subclasses and demonstrate their functionalities.

# class Employee:
#     def _init_(self, name, salary):
#         self.name = name
#         self.salary = salary

# class Manager(Employee):
#     def role(self):
#         print(f"{self.name} is a Manager")

# class Developer(Employee):
#     def role(self):
#         print(f"{self.name} is a Developer")

# # Instantiate and call methods
# manager = Manager("Alice", 80000)
# manager.role()

# developer = Developer("Bob", 60000)
# developer.role()