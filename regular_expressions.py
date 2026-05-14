# Regular expression, called regex for short, are a sort of mini language that describes a pattern of text.
"""
The general process of using regular expressions in Python involves 4 steps:
1. Import the re module
2. Pass the regex string to re.compile() to get a Pattern object
3. Pass the text string to the Pattern object's search() method to get a Match object.
4. Call the Match object's group() method to get the string of the matched text.
"""
import re
phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_pattern.search('My number is 413-666-1234')
print(match_obj.group())

# Grouping with Parentheses
# Adding parantheses will create `groups` in the regex string
# By passing integer to the `group()` method, we can grab different parts of the matched text.
# Passing 0 or nothing to the group() method will return the entire matched text.
phone_re = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_re.search('My number is 413-666-1234')
print(mo.group(1)) # return the 1st group
print(mo.group(2)) # return the 2nd group
print(mo.group()) # return the full matched text

# To get all the groups at once, you can use the groups() method.
print(mo.groups()) 
print()

# Naming the groups with (?P<group_name>pattern)
phone_re = re.compile(r'(?P<area>\d{3})-(?P<prefix>\d{3})-(?P<line>\d{4})')
mo = phone_re.search('My number is 413-666-1234')
print(mo.group('area'))
print(mo.group('prefix'))
print(mo.group('line'))
print(mo.group()) # return the full matched text
print(mo.groups()) # return all the groups
print(mo.groupdict()) # return all the groups as a dictionary

# If you want to use ( and ) in regex use the `\` with them.

"""
The `|` character is called a pipe, and it's used as the alternation operator in regular expressions.
We can use it anywhere we want to match one of multiple expressions.
"""
print('\nAbout `|` pipe: ')
pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
match = pattern.search('Catch me if you can.')
print(match.group())
print(match.group(1))

"""
In addition to a search() method, Pattern objects have a findall() method.
While search() will return a Match object of the first matched text in the searched string, the findall() method will return the strings of every match in the searched string.
The findall() method returna a list of strings as long as there are no groups in the regular expression.
"""
print('\nAbout findall() method: ')
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# If there are groups in the regular expression, then findall() will return a list of tuples
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # This regex has groups.
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))


"""
We can define a set of characters to match inside square brackets.
This set is called a `character class.`
"""
print('\nAbout `[]`: ')
vowel_pattern = re.compile(f'[aeiouAEIOU]')
print(vowel_pattern.findall('RoboCop eats BABY FOOD.'))
# You can also include ranges of letters or numbers by using a hyphen.
# For example, the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.

# By placing a caret character (^) just after the character class's opening brackets, we can make a negative character class.
consonant_pattern = re.compile(r'[^aeiouAEIOU]')
print(consonant_pattern.findall('RoboCop eats BABY FOOD.'))

"""
\d -> Any numeric digit from 0 to 9
\D -> Any character that is not a numeric digit from 0 to 9.
\w -> Any letter, numeric digit, or the underscore character. 
\W -> Any character that is not a letter, numeric digit, or the underscore character.
\s -> Any space, tab, or newline character.
\S -> Any character that is not a space, tab, or newline character.
"""

print()
# The . (or dot) character in a regular expression string matches any character except for a newline.
at_re = re.compile(r'.at')
print(at_re.findall('The cat in the hat sat on the flat mat.'))

# The ? character flags the preceding qualifier as optional.
pattern = re.compile(r'42!?')
print(pattern.search('42!'))
print(pattern.search('42'))
# To make multiple characters optinal, place them in a group and put the ? after the group.

# The * (called the star or asterisk) means “match zero or more.”
# In other words, the qualifier that precedes the star can occur any number of times in the text.
# It can be completely absent or repeated over and over again. 

# The + (or plus) means “match one or more.”

# These 2 regular expressions are same:
# (Ha){3,5}
# (HaHaHa)|(HaHaHaHa)|(HaHaHaHaHa)

"""
Greedy vs Non-Greedy Matching:
By default, regular expressions are greedy, meaning they will match as many characters as possible.
To make a regex non-greedy, you can add a ? after the qualifier.
For example, the regex .*? will match as few characters as possible.
"""
print('\nAbout greedy and lazy: ')
greedy_pattern = re.compile(r'(Ha){3,5}')
match1 = greedy_pattern.search('HaHaHaHaHa')
print(match1.group())

lazy_pattern = re.compile(r'(Ha){3,5}?')
match2 = lazy_pattern.search('HaHaHaHaHa')
print(match2.group())

"""
The dot in .* will match everything except a newline.
By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.
"""
newline_re = re.compile('.*', re.DOTALL)
print(newline_re.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

"""
You can use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. 
Likewise, you can put a dollar sign ($) at the end of the regex to indicate that the string must end with this regex pattern. 
"""
whole_string_is_num = re.compile(r'^\d+$')
print(whole_string_is_num.search('12345xyz67890') == None)

"""
You can also use \b to make a regex pattern match only on a word boundary: the start of a word, end of a word, or both the start and end of a word.
In this case, a “word” is a sequence of letters separated by non-letter characters. 
"""
print()
bat_re = re.compile(r'\bbat\b')
print(bat_re.findall('The bat sat on the mat.'))
print(bat_re.findall('The batmobile sat on the mat.'))

#The \B syntax matches anything that is not a word boundary
print()
bat_re = re.compile(r'\Bbat\B')
print(bat_re.findall('The bat sat on the mat.'))
print(bat_re.findall('The abatmobile sat on the mat.'))

"""
Normallly, regular expressions match text with the exact casing we specify.
To make our regex case-insensitive, we can pass `re.IGNORECASE` or `re.I` as a second argumnet to re.compile().
"""
print()
pattern = re.compile(r'robocop', re.I)
print(pattern.search('RoboCop is part man, part machine, all cop.').group())
print(pattern.search('ROBOCOP protects the innocent.').group())
print(pattern.search('Have you seen robocop?').group())

# Substituting String
agent_pattern = re.compile(r'Agent \w+')
secret_agent = agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob.')
print(secret_agent)
# To substitute certain groups
agent_pattern = re.compile(r'Agent (\w)\w*')
secret_agent = agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.')
print(secret_agent)

# Managing Complex Regex with Verbose Mode
pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    \d{3}  # First three digits
    (\s|-|\.)  # Separator
    \d{4}  # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)