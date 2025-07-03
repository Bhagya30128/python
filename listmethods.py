"""
list is a collection/group of items /values /elements they can be enclosed within the squarebrackets[] sperated by (,)
list methods: append/extend/count/mutability/index/remove/pop/insert
syntax: listname.methodname()
"""

#append: this method is used to add the elements
list = ["Edinburgh", "Scotland","iondon"]
print(list)
list.append("bhrihimgam")
print(list)

# extend: the method is used to add the elements at the end but
# as a sublist
list.extend(["Paris", "Malta", "Aus"])
print(list)

#count: This methods counts the number of repeated elements in a list
flowers = ["rose","mary","rose","jasmine","hibiscus"]
flowers.count("rose")
print(flowers)

#mutability:changing the elements
mylist4 = ["hello","ece",123,34,56,56+78j]
print(mylist4)
mylist4[2] = "agri"
print(mylist4)

# pop-- remove the elements using index
mylist5 = [12,34,565,78.9,34+56j,"hello"]
print(mylist5)
mylist5.pop(2)
print(mylist5)

#remove-- remove the elements directly
mylist5.remove(34)
print(mylist5)


#count-- itcounts the number of occurance of a item in a list
mylist6 = [22,33,33,22,55,22,44,67,56,22]
print(mylist6.count(22))
"""note" it will take atmost only one arugument"""

#insert -- it just inserts the elements into the list using the index
mylist7 = [22,33,44,77,88]
print(mylist7)
mylist7.insert(1,"hello")
print(mylist7)
"""note: in insert method no element is removed theey just replaces the position"""

#index-- this method tells the position it tells the first occurance when an element is repeated
mylist8 = [22,44,55,55,44,66,67,89]
print(mylist8.index(44))#1
print(mylist8.index(55))#2
#reverse--it just reverse the elements
mylist8.reverse()
print(mylist8)
#copy--it just coyp the elements in a list 
mylist9 = [22,33,44,55,66,77]
print(mylist9)
mylist10 = mylist9.copy()
print(mylist10)
#clear -- it just clear the elements in a list
print(mylist10.clear())
print(mylist10)

#sort-- it just arranges the elements in a sorting way
mylist11 = [22,11,77,9,89,0]
mylist11.sort()
print(mylist11)
mylist12 = ["m","a","k","b","c","s","k","j"]
mylist12.sort()
print(mylist12)
#mylist13 = [12,123,"hello"]
#mylist13.sort()
# in buit functions
mylist12 = [23,34,56,89]
print(len(mylist12))
print(max(mylist12))
print(min(mylist12))
print(sum(mylist12))
