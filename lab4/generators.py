#1
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

# Example usage:
N = int(input("Enter a number: "))
for square in square_generator(N):
    print(square)

#2
def even_number_generator(n):
    for i in range(0, n + 1, 2):
        yield i

# Get user input
n = int(input("Enter a number: "))

# Generate even numbers and print in comma-separated format
print(",".join(map(str, even_number_generator(n))))

#3
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Get user input
n = int(input("Enter a number: "))

# Use generator to print numbers
print("Numbers divisible by 3 and 4:", list(divisible_by_3_and_4(n)))

#4 
def squares(a, b):
    """Generator to yield squares of numbers from a to b (inclusive)."""
    for i in range(a, b + 1):
        yield i ** 2

# Get user input for range
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

# Using the generator with a for loop
print("Squares of numbers from", a, "to", b, ":")
for square in squares(a, b):
    print(square)

#5 
def countdown(n):
    """Generator to yield numbers from n down to 0."""
    for i in range(n, -1, -1):
        yield i

# Get user input
n = int(input("Enter a number: "))

# Using the generator with a for loop
print("Countdown from", n, "to 0:")
for num in countdown(n):
    print(num)
