""" tuples is a collection of items/value/elements they are enclosed within the parenthesis or open brackets () by (,)
As tuples are imutable it mean we can't change so when the data is fixed we can go with tuple
"""
#eg1:
mytuple = (13,12,11)
print(type(mytuple))#<class tuple>
mytuple2 = () #empty tuple
print(type(mytuple2))#<class tuple>
mytuple3 = (10)
print(type(mytuple3))#<class tuple>
"""
note: when you wanna create a tuple with single value it should be separated by so that the complier 
treats as tuple or else it just treats integer 
"""
#syntax: tuplevariable = (val1, val2, val3,....,valn)
mytuple5 = (12,23,45,34+78j,"hello",(123,"ece"))
mytulpe6 = (45,)
print(type(mytulpe6))

#cerating the tuple with a single element
t = [23,45,"jj"]
print(t)
k = (tuple)
print(k)
# creating the tuple with "tuple" predefined word
t = tuple()#it consider as a empty tuple
print(t)

# Accesing the elements in a tuple: Using the index we can acess the elements in a tuple
#index syntax(star:stop)
mytuple8 = (11,22,44,55,77,(78,89),"hello")
print(type(mytuple8))
print(mytuple8[0:5])
print(mytuple8[0:3])

mytuple9 = ([12,13,14],[89,90,78])
print(mytuple9[1])
# Slicing -- it is used to retrive the elements from a particular range the 
#syntax(start:stop:skip)s^3
mytuple10 = (11,12,33,44,55,77,88,99,"hello","agri","ECE")
print(mytuple10[3:9:3])

mytuple11 = (22,33,44,66,77,88,99,10,24,24,)
print(mytuple11[4:10:5])

mytuple12 = ("hello",123,456,45,34.45,56+78j,"ists","agri","ece",345.9,"dept",12,23,34,56,67,90)
print(mytuple12[-1])
print(mytuple12[7:-2:2])
#note: indexs are 2 types 
# positive indexing and forward indexing which always starts with 0 from lefthand side direction 
# negative indexing and backward indexing which always starts with -1 from righthand side direction 

mytuple13 = (12,[12,13],[10,20])
print(mytuple13)
print(mytuple13[1][1])
print(mytuple13[2][1])

mytuple14 = (12,18,14,15,[16,17,18],[12,13,15])
print(mytuple14)
print(mytuple14[5][1]) 