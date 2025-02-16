# Python Casting
x = int(3.8)  # Converts float to int
print(x)  # Output: 3

# Python Strings
s = "Hello, Python!"
print(s.upper())  # Output: HELLO, PYTHON!

# Python Booleans
is_active = True
print(is_active and False)  # Output: False

# Python Operators
a, b = 10, 3
print(a + b)  # Addition, Output: 13

# Python Lists
lst = [1, 2, 3]
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]

# Python Tuples
tup = (1, 2, 3)
print(tup[1])  # Output: 2

# Python Sets
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

# Python Dictionaries
d = {"name": "Alice", "age": 25}
print(d["name"])  # Output: Alice

# Python If...Else
x = 10
if x > 5:
    print("Greater than 5")
else:
    print("Less or equal to 5")  # Output: Greater than 5

# Python While Loops
i = 1
while i < 4:
    print(i)
    i += 1  # Output: 1 2 3

# Python For Loops
for num in range(3):
    print(num)  # Output: 0 1 2

# Python Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))  # Output: Hello, Bob!

# Python Lambda
square = lambda x: x * x
print(square(4))  # Output: 16
