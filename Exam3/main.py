#Questions

#Вопрос 1
# класс ва объект дар Python ин

#Вопрос 2
# Атрибуты
# Атрибутҳои класс ва атрибутҳои объект бо хам бо он фарк мекунанд ки мо атрибутхои классро дар хамачои класс истифода бурда метонем атрибутхои обект бошанд танхо дар даруни обект

#Вопрос 3
# Инкапсуляция
# Инкапсуляция ин яке аз принсипхои OOP мебошад ва барои атрибутҳоро private(махфӣ) ё protected(ҳифзшуда) кардан истифода бурда мешавад
# Барои атрибутхоро private(махфӣ) кардан __атрибут ва барои protected(ҳифзшуда) кардан _атрибут бояд кунем

#Вопрос 4
# Наследование
# Наследование ин яке аз принсипхои OOP мебошад ва барои меросгири яъне чанд бор 1 кодро нанависи факат номи classro фарёд мекуни ва кодхои онро дар класси худ мегири ва агар хости ба он тагйиру иловахо дохил мекуни
# class salom :
#   pass
# class alek(salom):
#   pass 


#Вопрос 5
# Полиморфизм
# Полиморфизм ин яке аз принсипхои OOP мебошад ва барои вакте Наследование мешавад дар методхои сlassi паретн тагйиру иловахи дохил куни
# class Car(ABC) :
#     def move(self) :
#         print("I move with gas")

# class Bike(Car) :
#     def move(self):
#         print("I move withought gas")

# car = Car()
# bike = Bike()
# car.move()
# bike.move()
# Мисоли иваз куни метод бо Полиморфизм








# from abc import ABC, abstractclassmethod

#TASK 1
# class BankAccount :
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self, amount) :
#         self.balance += amount
#         print("Deposit succefully")
    
#     def withdraw(self, amount) :
#         if self.balance < amount :
#             print("Money not enought")
#         else :
#             self.balance -= amount
#             print("Withdrow succesfully")
#     def __str__(self):
#         return f"{self.owner} --> {self.balance}"

# bank = BankAccount("Ehson", 1000)
# print(bank)
# bank.deposit(200)
# print(bank)
# bank.withdraw(300)
# print(bank)

#TASK 2
# class Student :
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
    
#     def is_passed(self) :
#         print(self.score >= 60)

#     def __str__(self):
#         return f"{self.name} --> {self.score}"

# student = Student("Abdurahmon", 70)
# print(student)
# student.is_passed()

#TASK 3
# class User :
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password
    
#     def check_password(self, p) :
#         print(p == self.__password)
    
#     def change_password(self, old, new) :
#         if self.__password == old :
#             self.__password = new
#             print("Password changed succefully")
#         else :
#             print("Wrong old passwprd")
    
#     def __str__(self):
#         return f"{self.username} --> {self.__password}"

# user = User("Abdurahmon", 123456)
# user.check_password(123456)
# user.change_password(123456, 12345678)
# print(user)

#TASK 4
# class Product :
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def total_price(self) :
#         print(self.price * self.quantity)
    
#     def __str__(self):
#         return f"Name: {self.name}. Price: {self.price}. Quantity: {self.quantity}"

# product = Product("Apple", 5, 10)
# product.total_price()
# print(product)

#TASK 5
# class Rectangle :
#     def __init__(self, length , width):
#         self.length = length
#         self.width = width
    
#     def area(self) :
#         print(self.length * self.width)

#     def perimeter(self) :
#         print(2 * (self.length + self.width))

#     def __str__(self):
#         return f"Width: {self.width}. Length: {self.length}"

# rectangle = Rectangle(10, 5)
# rectangle.area()
# rectangle.perimeter()
# print(rectangle)

#TASK 6
# class Car :
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
    
#     def info(self) :
#         print(f"Brand: {self.brand}. Year: {self.year}")

#     def __str__(self):
#         return f"Brand: {self.brand}. Year: {self.year}"

# car = Car("MERC", 2024)
# car.info()
# print(car)

#TASK 7
# class Car(ABC) :
#     def move(self) :
#         print("I move with gas")

# class Bike(Car) :
#     def move(self):
#         print("I move withought gas")

# car = Car()
# bike = Bike()
# car.move()
# bike.move()

#TASK 8
# class Shape :
#     def area(self) :
#         pass

# class Rectangle(Shape) :
#     def __init__(self, width, heigth):
#         super().__init__()
#         self.width = width
#         self.heigth = heigth

#     def area(self):
#         print(self.width * self.heigth)

# class Circle(Shape) :
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius
#     def area(self):
#         print(3.14 * (self.radius ** 2))

# rectangle = Rectangle(10, 5)
# circle = Circle(10)
# rectangle.area()
# circle.area()

#TASK 9
# class Transport :
#     def speed(self, speed) :
#         pass

# class Plane(Transport) :
#     def speed(self, speed):
#         print(f"Speed: {speed}")

# class Train(Transport) :
#     def speed(self, speed):
#         print(f"Speed: {speed}")

#TASK 10
# class Book :
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
    
#     def info(self) :
#         print(f"{self.author} --> {self.title}")

#     def __str__(self):
#         return f"{self.author} --> {self.title}"

# book = Book("Maktabi kuhna", "Sadriddin Ayni")
# book.info()
# print(book)