""""""
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
