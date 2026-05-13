# String are immutable data types.
# String literals -> the string vales that literally appear in our code.
s1 = 'Hello World'
s2 = "Hello World"
s3 = """
Hello World
""" # -> Multiline String
print(s3)

# Escape Sequences
# \' -> single quote
# \" -> double quote
# \\ -> backslash
# \n -> newline
# \t -> tab
print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw Strings -> makes it easier to enter string values that have backslashes by ignoring all the escape sequences.
print(r'C:\Users\User\strings.py')

"""
This is a multililne comment
"""
print()
# Indexes and Slices
"""
'   H  e   l   l   o  ,     w  o  r  l  d   !  '
    0  1   2   3   4  5  6  7  8  9 10  11 12
  -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1
"""
greetings = 'Hello, world!'
print(greetings[0]) # -> index
print(greetings[0:5]) # -> slicing (end index is exclusive)
print(greetings[7:-1]) # -> slicing
# Slicing doesn't modidy the orginal string.

print()
print('Hello' in greetings) # -> Membership Operator
print('Hello' not in greetings)

print()
# f-string -> let you place varaible name or entire expression within a string.
name = 'John'
age = 20
print(f'Hello {name}, you are {age} years old.')
print()

# String interpolation -> strings included as %s format specifier that Python would replace with another string.
print('Hello %s, you are %d years old.\n' % (name, age))

# format() string method
print('Hello {}. you are {} years old\n'.format(name, age))

# USEFUL STRING METHODS
# upper() -> returns a new string with all characters in uppercase
# lower() -> returns a new string with all characters in lowercase
print(name.upper())
print(name.lower())
# isupper() -> returns True if all characters in the string are uppercase
# islower() -> returns True if all characters in the string are lowercase
print(name.isupper())
print(name.islower())
# capitalize() -> returns a new string with the first character capitalized and the rest in lowercase
print(greetings.capitalize())
# title() -> returns a new string with the first character of each word capitalized
print(greetings.title())
# startswith(sub) -> returns True if the string starts with the specified substring
print(greetings.startswith('Hello'))
# endswith(sub) -> returns True if the string ends with the specified substring
print(greetings.endswith('world!'))
# join(iterable) -> returns a new string by concatenating the elements of an iterable with the string as a separator
print(' '.join(['Hello', 'world!']))
# split(sep) -> returns a list of strings by splitting the string at the specified separator
print(greetings.split(' '))
# strip() -> returns a new string with leading and trailing whitespace removed
print('  Hello, World!  '.strip())
# lstrip() -> returns a new string with leading whitespace removed
print('  Hello, World!  '.lstrip())
# rstrip() -> returns a new string with trailing whitespace removed
print('  Hello, World!  '.rstrip())
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS')) # Strip in occurrences of 'a','m','p','S' from the start or end of the string.

print()
# ord() -> returns the ASCII value of a character.
print(ord('a'))
# chr() -> returns the character with the specified ASCII value.
print(chr(97))

# Copying and Pasting Strings
"""
The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s clipboard.
Sending the output of your program to the clipboard will make it easy to paste it into an email, a word processor, or some other software.
"""
import pyperclip
pyperclip.copy('Hello, world!')
paste = pyperclip.paste()
print(paste)