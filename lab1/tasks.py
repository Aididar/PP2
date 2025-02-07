
#1
print("Hello, World!")

#2
if 5 > 2:
  print("Five is greater than two!")

#This is a comment
print("Hello, World!")

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = 5
print(type(x))

#numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#strings
a = "Hello"
print(a)
#2
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#3
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#4
b = "Hello, World!"
print(b[2:5])
#5
a = "Hello, World!"
print(a.upper())
#6
a = "Hello, World!"
print(a.replace("H", "J"))
#7
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#8
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#9
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#10 The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#variables
x = 5
y = "John"
print(x)
print(y)

#2
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#3 
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#4 
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
