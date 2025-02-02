#1
class StringManipulator:
    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())
#2
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
#4
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to the balance. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
#6
def prime(num):
    if num < 2:
        return False
    for i in range(2, num ):
        if num % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7]
prime_numbers = list(filter(lambda x: prime(x), numbers))



