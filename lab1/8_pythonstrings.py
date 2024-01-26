#ex1
print("ainaz")
print('ainaz')
#ex2
a="ainaz"
print(a)
#ex3
a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#ex4
a='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#ex5
a="ainaz"
print(a[1])
#ex6
for x in "ainaz":
  print(x)
#ex7
a="ainaz"
print(len(a))
#ex8
txt="The best things in life is ainaz!"
print("ainaz" in txt)
#ex9
txt="The best things in life is ainaz!"
if "ainaz" in txt:
  print("Yes, 'ainaz' is present.")
#ex10
txt = "The best things in life is ainaz!"
print("other" not in txt)

#slicing strings
#ex1
b="hello, ainaz!"
print(b[2:5])
#ex2
b = "Hello, ainaz!"
print(b[:5])
#ex3
b = "Hello, ainaz!"
print(b[2:])

#modify strings
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

#string concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#format strings
age = 17
txt = "My name is aianz, and I am {}"
print(txt.format(age))

#escape characters
txt = "We are the so-called \"Vikings\" from the north."
"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""
