# Ques 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alex", 25)

print("Name:", person1.name)
print("Age:", person1.age)


# Ques 2

class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account balance for {self.customer_name}: {self.balance}")
        return self.balance
    
account = BankAccount("123456789", "Alice", 1000)
account.deposit(500)
account.withdraw(300)
account.check_balance()


# Ques 3

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(", ")
        return cls(title, author)

book = Book.from_string("Python Programming, John Doe")

print("Title:", book.title)
print("Author:", book.author)


# Ques 4

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("dog sound")

class Cat(Animal):
    def sound(self):
        print("cat sound")

dog = Dog()
cat = Cat()

dog.sound() 
cat.sound()


# Ques 5

class A1:
    def m1(self):
        print("A1 class")

class A2:
    def m2(self):
        print("A2 class")

class A3(A1, A2):
    def m3(self):
        print("A3 class")

a3 = A3()

a3.m1()       
a3.m2()   
a3.m3()
