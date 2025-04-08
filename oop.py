
# class Person():
#     def __init__(self,name,age):

#         self.name = name
#         self.age = age
    
#     def introduction(self):
#         return f"Hi, my name is {self.name} and I am {self.age} years old."
    


# p1 = Person('Himanshu', 23)

# print(p1.introduction())



# class BankAccount():
#     def __init__(self, account_holder):
#         self.account_holder = account_holder
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    
#     def withdrawal(self,amount):
#         self.balance -= amount
#         return self.balance
    

# acc = BankAccount("himanshu")
# acc.deposit(1000)
# print(acc.withdrawal(700))


        
# class Car():
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.speed = 0
    
#     def accelerate(self, amount):
#         self.speed += amount
#         return self.speed
    
#     def brake(self, amount):
#          self.speed -= amount
#          if self.speed < 0:
#              self.speed(0)
           
        

# car1 = Car("Toyota", "corola", 2022)
# car1.accelerate(40)
# car1.brake(15)
# print(car1.speed)





# class Animal():
#     def __init__(self, name):
#         self.name = name
        
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def make_sound(self):
#         super().make_sound()
#         print("woof")

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def make_sound(self):
#         super().make_sound()
#         print("meow")

# dog = Dog("robex")
# dog.make_sound()


# class Book:
#     def __init__(self, title, author, available=True):
#         self.title = title
#         self.author = author
#         self.available = available  # Use the provided argument value

#     def __str__(self):
#         return f"'{self.title}' by {self.author} - {'Available' if self.available else 'Borrowed'}"

# class Library:
#     def __init__(self):
#         self.books = []  # Library will store a list of books

#     def add_book(self, book):
#         self.books.append(book)  # Add book object to the list
#         print(f"Book '{book.title}' added to the library.")

#     def borrow_book(self, title):
#         for book in self.books:
#             if book.title == title and book.available:
#                 book.available = False  # Mark the book as borrowed
#                 print(f"You have borrowed '{book.title}'.")
#                 return book
#         print(f"Sorry, the book '{title}' is not available.")
#         return None

#     def return_book(self, title):
#         for book in self.books:
#             if book.title == title and not book.available:
#                 book.available = True  # Mark the book as available again
#                 print(f"You have returned '{book.title}'.")
#                 return book
#         print(f"Sorry, '{title}' was not borrowed from this library.")

#     def show_books(self):
#         if not self.books:
#             print("The library has no books.")
#         else:
#             for book in self.books:
#                 print(book)  # Calls __str__() method of Book class

# # Example Usage
# library = Library()

# # Creating book objects
# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")

# # Adding books to the library
# library.add_book(book1)
# library.add_book(book2)

# # Borrowing and returning books
# library.borrow_book("1984")
# library.show_books()  # Show all books in the library
# library.return_book("1984")
# library.show_books()  # Show all books again


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner         # Public attribute
#         self.__balance = balance   # Private attribute (Encapsulation)

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive!")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
#         else:
#             print("Invalid withdrawal amount!")

#     def get_balance(self):  # Getter method
#         return self.__balance

# # Creating an object
# account = BankAccount("John", 1000)

# # Accessing public attribute
# print(account.owner)  

# # Trying to access private attribute (Fails)
# # print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# # Accessing private data via method
# print("Balance:", account.get_balance())  

# # Performing transactions
# account.deposit(500)
# account.withdraw(200)




# class Car:
#     def __init__(self, brand, speed, model):

#         self.__brand = brand
#         self._speed = speed
#         self.model = model
        
#     def acceleration(self,amount):
#         if self._speed >= 0:
#             self._speed += amount

#         else:
#             print("the car is off")

#     def getter(self):
#         return self.__brand
    
# car = Car("bmw", 50, "2025")

# # print(car._brand)
# print(car.getter())


# from abc import ABC, abstractmethod

# class Shape(ABC):
#     def __init__(self, length, width):
#         super().__init__()
#         self.length = length
#         self.width = width

#     @abstractmethod
#     def area(self):
#         print("# reason bcoz we have just blueprint so you do not have to implement this in Abstract cals")
#         pass   

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, length, width):
#         super().__init__(length, width)

#     def area(self):
#         return super().area()
#         my_area = self.length * self.width
#         return my_area
    
#     def perimeter(self):
#         return super().perimeter()
#         return 2(self.length+self.width)

# circle = Circle(5,7)
# print(circle.area())






class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP is starting...")

class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)  # Composition: Car HAS-A Engine

    def drive(self):
        self.engine.start()  # Using Engine's method
        print(f"The {self.brand} car is now driving.")

# Creating a Car object
my_car = Car("Toyota", 150)
print(my_car.engine)
my_car.drive()
