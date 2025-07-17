#FUNCTIONS:- Function is a block of code. it is excueted when it is called in python to create function 
#def keyword is used function. def is nothing but different
"""
def function name():
    statement/functionbody
function calling()
"""
def bhagya():# functiondefination
    print("good morning")
bhagya()

#note: the value that was passed into function defination is called parameters.
# the value that was passed into function calling is called argument.
#passing parameter and argument is a function.
def function(a):#parameter
    print("this is value",a)
function(100)#functioncalling

#single parameter function: passing a single or one parameter function
def funtion(c):
    print(c)
function(30)

#multiple parameter function: passing a multiple values to a function is called as multiple parametres function
def function3(a,b):
    print("the value:",a+b)
function3(30,28)

#Perform a float division oparetion using function name  float division operation
def function(a,b):
    print("The value:",a/b)
function(3.8,5.4)

# write a program to wish a person using tha python function 
def function():
    print("Happy Birthday to you Gundamma(Amrutha)")
function()

# Give a short  note on python function parameter 
# FUNCTION: Function is a block of code. Function Parameters are variables that are specified within the parentheses of a function definition
# it's excueted when it's called in python to create function. def keyword is used function. def is nothing but different

""" Arbitary argument(): Arbitary argument is an argument which is denoted by (*).
    which takes multiple argument for a single parameter and returns the result in the form of tuple.""" 
#parameter error of positional argument
#def function(a):
 #   print(a)
#function(12,15,20)
def function(*a):
    print(a)
function(30, 28, 25)

# Key arguments(**): key argumnet is function which takes single parameter for a multiple argument
# in the form of key value place so that output is in dictinaty. 
def function(**name):
    print("Hi", name)
function(name = "Bhagya",place = "Tanuku")

#Nested function:- A function within a function iscalled nested functions
def outerfunction():
    print("outerfunction statement")
    def innerfunction():
        print("innerfunction statement")
    innerfunction()
outerfunction()

def outerFunction():
    print("Hello")
    def innerFunction():
        print("Bhagya Sri Lakshmi")
    innerFunction()
outerFunction()




