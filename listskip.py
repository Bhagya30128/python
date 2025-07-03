"""
Slicing in used to retrieve the element from one particular range to another particular range
The syntax: s^3(start:stop:skip)
"""

mylist = [1,2,13,16,17,18,19]
print(mylist)
print(mylist[0:6:2])

mylist1 = [2,5,6,7,8,9,10]
print(mylist1[0:7:3])

mylist2 = [45,46,78,90,56,34,78,90,34,65,89]
print(mylist2[0:8:4])

mylist3 = ["hello", 12,34,56,89.90,456+5j,4555,789]
print(mylist3[2:6:2])