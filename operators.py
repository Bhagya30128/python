"""
An operator is a special symbol. Which is used to perform to operation 
Ex:- c = a+b
here c, a, b are operator + is aspecial symbol
"""
# the operators types
#Arthimetic Operator
#Relational Operator
#Bitwise Operator
#Identity Operator
#Membership Operator
#Assignment Operator

#Arthimetic Operator is used to perform some mathematical (or) Arthimetic Operation.
# The Operators are +, -, *, /, //, %, **.

a = int(input("enter a number:"))
b = int(input("enter a number:"))
print("The addition", a+b)
print("The subtraction", a-b)
print("The multiplication", a*b)
print("The division", a/b)
print("The floor division", a//b)
print("The modular", a%b)
print("The power", a**b)

#Relational operators are used to compare the values and return the boolean they are >, <, >==, <==, ==, !=

a = int(input("enter a number:"))
b = int(input("enter a number:")) 
print("The greater value", a>b)
print("The lesser value", a<b)
print("The greater than or equals value", a>=b)
print("The lesser than or equals value", a<=b)
print("The equals too value", a==b)
print("The not equals too value", a!=b)

# Logical operators are used to perform logical operations. They are logical and, or, not
# and -- if both the condition are true it returns the true.
# T T T
# F T F
# T F F
# F F F
# or-- if one of the condintion is true it returns the true.
# T F T
# F T T
# T T T
# F F F
# not-- it just negotiates the condition
# T F
# F T

a = 13
b = 45
c = a>=35 and b<=50
print(c)
d = 67
e = 89
f = d!=67 or e==89
print(f)
g = 10
print(not(g)) #F
h = 0
print(not(h)) #F

# Bitwise operators are used to perform binary operations they are:
# bitwise and (&): if both the bits are "1" it returns "1"
# bitwise or (|): if one the bits are "1" it returns "1"
# bitwise xor (^): if both the bits are "1" it returns "1" and if both the bits are "1" it returns "0"

a = 5
b = 9
c = a&b
print(c)
d = 15
e = 13
f = d/e
print(f)
g = 12
h = 14
i = g^h
print(i)

#Membership operators are used to check the values in a sequence. and returns the boolean values. 
# they operators are "in", "not in"

X = ["apple", "banana"]
print("apple" in X)
print("pp" not in X)
print("banana" not in X)
print("dragon" in X)

# Identity  operators are used to compare the values. and return the boolean values the operators are "is", "is not".

x = [1, 2, 3]
y = [4, 5, 6]
z = x
print(x is y) #F
print(x is z) #T
print(y is z) #F
print(y is not z) #T
print(z is not y) #F
print(x is not y) #T