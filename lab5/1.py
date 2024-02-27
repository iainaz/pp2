#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
def match_ab(s):
    pattern = r'ab*'
    if re.fullmatch(pattern, s):
        return True
    return False
#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
def match_abb(s):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, s):
        return True
    return False
#Write a Python program to find sequences of lowercase letters joined with an underscore.
def find_lowercase_sequences(s):
    pattern = r'[a-z]+(_[a-z]+)+'
    return re.findall(pattern, s)
#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def find_uppercase_sequences(s):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, s)
#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
def match_a_anything_b(s):
    pattern = r'a.*b$'
    if re.fullmatch(pattern, s):
        return True
    return False
#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
def replace_with_colon(s):
    return re.sub(r'[ ,.]', ':', s)
#Write a python program to convert snake case string to camel case string.
def snake_to_camel(s):
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
#Write a Python program to split a string at uppercase letters.
def split_at_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)
#Write a Python program to insert spaces between words starting with capital letters.
def insert_spaces(s):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s)
#Write a Python program to convert a given camel case string to snake case.
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()