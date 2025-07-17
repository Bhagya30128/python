"""
STRING:-String is a collection of characters and a character is simple a symbol for example 
the engilsh language has 26 characters and computer don't deel with character 
they deel with binary numbers even now may see character on screen internally,
it's stored and maniplated as a combination "0" and "1"
"""
a = "bhagya sri lakshmi"
print(a[0:11])
print(a[2:18:3])

#Representation to a string:- (' ') (" ") (""" """)
v = 'IT'
print(type(v))

v1 = "ECE"
print(type(v1))

v2 = """ISTS""" 's'
print(type(v2))

#String method 
# syntax: variablename.method()
# 1.upper(): Converts form lower to upper case
w = "python"
print(w.upper())

# 2.lower(): Coneverts from upper to lower case
w1 = "python"
print(w1.lower())

# count method: This methond is used to count the repeated wordin the string.
m = "I love prasanthi prasanthi"
print(m.count("prasanthi"))

# index method: This method is used to return the index position of a string.
n = "vijayavada"
print(n.index("j"))

#Strip: This method is used to remove the spaces in the string.
s1 = " this is my book "
print(len(s1))
print(s1)
s2 = s1.strip()
print(len(s2))

# two types of strips 
# 1.rstrip: This method is used to remove the right side spaces in the string.
s1 = " this is my room "
print(len(s1))
print(s1)
s2 = s1.rstrip()
print(len(s2))
print(s2)

# 2.lstrip: This method is used to remove the left side spaces in the string.
s1 = " this is my door "
print(len(s1))
print(s1)
s2 = s1.lstrip()
print(len(s2))
print(s2)

# format(): This method is used to return the string in a automated/real/format.
names = ["Bhagya", "Prasanthi", "Harini", "Kavya"]
for i in names:
    print("Hi {} Tinnava?" .format(i))

# Find method(): This methodis used to returns the -1 when the string element is not present
n = "bhagya"
print(n.find("b"))
print(n.find("y"))

#startswith(): when the string is startswith given string it return true.
#when the string is startswith given string with existing string.
n = "I Love My Self"
print(n.startswith("I"))#True
print(n.startswith("L"))#False

#endswith(): when the string is endswith given string it return true.
#when the string is endswith given string with existing string.
m = "i love python"
print(m.endswith("n"))#True
print(m.endswith("p"))#Fasle

#variablename.method():
websites = ["amazon.com","myntra.in","ojio.in"]
in_websites = []
for i in websites:
    if i .endswith(".in"):
        in_websites.append(i)
print(in_websites)

#isalpha(): it checks the if the all the character is string are alphabates are not it return the boolean values.
print("openai".isalpha())#True
print("openai123".isalpha())#False
print("open ai".isalpha())#False 

#isalnum() checks if all characters in the string are alphanumeric that is letters or numbers.
print("openai123".isalnum())#True
print("openai!".isalnum())#False
print("openai 123".isalnum())#False 

#title(): It's just return the given string
S = "the wing of five"
print(S.title())

#split(): it split the given string into list
s = "bhagya"
print(s.split())

#join(): it joins the splited list into string.
s1 = "  ".join(s)
print(s1)



