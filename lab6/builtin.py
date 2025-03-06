#1
import math

def multiply_list(numbers):
    return math.prod(numbers)

# Example usage
nums = [2, 3, 4, 5]
print(multiply_list(nums))  # Output: 120

#2
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# Example usage
text = "Hello World"
upper, lower = count_case(text)
print(f"Uppercase: {upper}, Lowercase: {lower}")  # Output: Uppercase: 2, Lowercase: 8

#3
def is_palindrome(s):
    return s == s[::-1]  # Reverse the string and compare

# Example usage
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

#4
import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  # Convert milliseconds to seconds
    return math.sqrt(number)

# Example usage
num, delay = 25100, 2123
print(f"Square root of {num} after {delay} milliseconds is {delayed_sqrt(num, delay)}")

#5
def all_true(t):
    return all(t)

# Example usage
print(all_true((True, True, 1, "hello")))  # Output: True
print(all_true((True, False, 1)))  # Output: False
