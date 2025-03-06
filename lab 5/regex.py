#1
import re

def match_pattern(s):
    return bool(re.fullmatch(r"^ab*$", s))

test_strings = ["a", "ab", "abb", "b", "abc", "aabb"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")

#2
import re

def match_pattern(s):
    return bool(re.fullmatch(r"^ab{2,3}$", s))

test_strings = ["abb", "abbb", "a", "ab", "abbbb", "abc"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")

#3
import re

def match_pattern(s):
    return bool(re.fullmatch(r"[a-z]+_[a-z]+", s))

test_strings = ["hello_world", "test_case", "Python_code", "hello_World", "no_underscore", "abc_def_ghi"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")

#4
import re

def match_pattern(s):
    return bool(re.fullmatch(r"[A-Z][a-z]+", s))

test_strings = ["Hello", "Test", "Python", "hello", "TEST", "P", "JavaScript"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")

#5 
import re

def match_pattern(s):
    return bool(re.fullmatch(r"a.*b", s))

test_strings = ["ab", "acb", "a123b", "axb", "a_b", "b", "abc", "a", "abb"]
for s in test_strings:
    print(f"{s}: {match_pattern(s)}")

#6
import re

def replace_chars(s):
    return re.sub(r"[ ,.]", ":", s)

# Test cases
test_strings = [
    "Hello world, how are you?",
    "Python is fun. Let's learn regex!",
    "Replace, spaces. commas and dots."
]

for s in test_strings:
    print(replace_chars(s))

#7
import re

def snake_to_camel(s):
    words = s.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

test_strings = ["hello_world", "convert_snake_case", "python_regex", "snake_to_camel"]

for s in test_strings:
    print(snake_to_camel(s))

#8
import re

def split_at_uppercase(s):
    return re.split(r"(?=[A-Z])", s)

test_strings = ["HelloWorld", "PythonIsFun", "SplitAtUppercase", "testString"]

for s in test_strings:
    print(split_at_uppercase(s))

#9
import re

def add_spaces(s):
    return re.sub(r"(?<!^)([A-Z])", r" \1", s)

test_strings = ["HelloWorld", "PythonIsFun", "InsertSpacesBetweenWords", "ThisIsATest"]

for s in test_strings:
    print(add_spaces(s))

#10
import re

def camel_to_snake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()

# Test cases
test_strings = ["helloWorld", "convertCamelCase", "pythonRegex", "camelToSnake"]

for s in test_strings:
    print(camel_to_snake(s))
