# # ####----List-----####

# # #list is a collection of items
# # #list is a changable/mutable data type
# # #list is a data structure
# # # list is a collection of items in a specific order
# # #list allow duplicate values

# # # eg: for list

# # list1 = [1,2,3,4,5,6,7,8,9,10]
# # print(list1)

# # list2 = ['a','b','c','d','e','f','g','h','i','j','a']
# # print(list2)

# # list3 =['a',3,True,6,"anu"]
# # print(list3)


# #find out the length of LIST

# # thislist = ["apple", "banana", "cherry"]
# # print(len(thislist))
# # print(type(thislist))

# # # list indexing

# list = ["a","b","c",1,2,23,5]

# print(list[0])
# print(list[-1])
# print(list[:])
# print(list[2:])
# print(list[:5])
# print(list[3:6])

# # a = [1,2,3]

# # b = a

# # print(b)


# # ---------------looping in list-----------


# thislist = ["apple", "banana", "cherry","orange"]
# for x in thislist:
#   print(x)
  
  
  
#   # *********************************************************************************************
  
  
  
#   ############------------PYTHON COLLECTIONS---------------#################

# # List is a collection which is ordered and changeable. Allows duplicate members.

# # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# # Dictionary is a collection which is ordered** and changeable. No duplicate members.




# ##----TUPLE-----

# # A tuple is a collection which is ordered and unchangeable.
# # in python tuples are written  with round brackets
# # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# # Tuple allow duplicate values
# # Tuple is ordered and unchangable
# # Tuple is a collection which is ordered and unchangeable.
# # we cannot add or remove items in tuple if once they created

# # tuple1 = ("abc", 34, True, 40, "male")
# # print(tuple1)
# # print(tuple1[0])
# # print(tuple1[-1])
# # print(tuple1[2:4])
# # print(tuple1[::-1])


# # tuple = ("apple", "banana", "cherry")
# # tuple2 = (1, 5, 7, 9, 3)
# # tuple3 = (True, False, False)

# # print(tuple)
# # print(tuple2)
# # print(tuple3)


# #  TYPE()

# # mytuple = ("apple", "banana", "cherry")
# # print(type(mytuple))

# # # TUPLE()

# # alist =["apple", "banana", "cherry"]
# # thistuple1 = tuple(alist)
# # print(thistuple1)

# # # TUPLE TO LIST

# # thislist = list(thistuple1)
# # print(thislist)


# #INDEXING

# # thistuple = ("apple", "banana", "cherry")
# # print(thistuple[1])



# # thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# # print(thistuple[2:5])
# # print(thistuple[:4])
# # print(thistuple[:])
# # print(thistuple[2:])
# # print(thistuple[2:-2])


# # # # NEGATIVE INDEXING
# # print(thistuple[-1])




# ###############------UPDATE TUPLE-----###############

# # x = ("apple", "banana", "cherry")
# # y = list(x)
# # y[1] = "kiwi"
# # x = tuple(y)

# # print(x)

# ############-------DELETE TUPLE----------############

# # tuple cannot allow delete.


# # ###----WE CAN APPLY ALL METHODS OF LIST BY CONVERT OUR TUPLE INTO LIST AND VICE VERSA

# # x = ("apple", "banana", "cherry")
# # y = list(x)
# # del y[1]
# # x = tuple(y)

# # print(x)

# #########-----Unpacking a tuple:-------##########

# # fruits = ("apple", "banana", "cherry")

# # (green, yellow, red) = fruits

# # print(green)
# # print(yellow)
# # print(red)

# ######----Add a list of values the "tropic" variable:

# # If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:



# # fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# # (green, *tropic, red) = fruits

# # print(green)
# # print(tropic)
# # print(red)


# #  ----JOINING THE TUPLES----

# # tuple1 = ("a", "b" , "c")
# # tuple2 = (1, 2, 3)

# # tuple3 = tuple1 + tuple2
# # print(tuple3)

# # ##----Multiply the fruits tuple by 2:

# # fruits = ("apple", "banana", "cherry")
# # mytuple = fruits * 3

# # print(mytuple)



# #######------TUPLE METHODS------##########

# # count()    Returns the number of times a specified value occurs in a tuple
# # index()    Searches the tuple for a specified value and returns the position of where it was found
# # len()      Returns the length of the tuple
# # max()      Returns the largest item in the tuple
# # min()      Returns the smallest item in the tuple
# # sorted()   Returns a sorted list of items in the tuple
# # reversed() Returns a reversed copy of the tuple
# # sum()      Sums the items of a tuple

# # COUNT()

# # thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# # x = thistuple.count(5)

# # print(x)

# # x = thistuple.index(8)

# # print(x)

# # x = thistuple.count()

# # print(x)

# # x = len(thistuple)

# # print(x)

# # x = max(thistuple)

# # print(x)

# # x = min(thistuple)

# # print(x)

# # x = sorted(thistuple)

# # print(x)

# # x = reversed(thistuple)

# # print(x)

# # # --------looping in tuple-------------


# # thistuple = ("apple", "banana", "cherry")

# # for i in range(len(thistuple)):
# #   print(thistuple[i])
  
  
  
# #   thistuple = ("apple", "banana", "cherry")
# # for x in thistuple:
# #   print(x)




# # *******************************************************************************************

# # ------------SET------------

# # myset = {"Apple","banana","Cherry","orange"}

# # print(myset)

# # # set items are unchangable, but you can remove items and add new items
# # #  duplicate values will be ignored:
# # # The values True and 1 are considered the same value in sets, and are treated as duplicates:
# # #sets can contain any type of objects,

# # thisset = {"apple", "banana", "cherry", "apple"}

# # print(thisset)



# # thisset = {"apple", "banana", "cherry", True, 1, 2}

# # print(thisset)
# # print(len(thisset))


# # # tuple construct to set

# # thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# # print(thisset)




# # # _--------- methods in sets----

# set={"apple","banana","cherry"}
# print(set)

# set1={"apple","banana","cherry"}
# set1.add("orange")
# print(set1)

set2={"apple","banana","cherry"}
set2.update(["orange","mango","grapes","cherry"])
print(set2)

# set3={"apple","banana","cherry"}
# set3.remove("banana")
# print(set3)

# set4={"apple","banana","cherry"}
# set4.discard("banana")
# print(set4)

# # set5={"apple","banana","cherry"}
# # if "apple" in set5:
# #     set5.remove("apple")
# # print(set5)    

# # set6={"apple","banana","cherry"}
# # set6.pop()
# # print(set6)

# # set7={"apple","banana","cherry"}
# # set7.clear()
# # print(set7)

# # set8={"apple","banana","cherry"}
# # set9=set8.copy()
# # print(set9)

# # thisset = {"apple", "banana", "cherry"}

# # print("banana" not in thisset)


# # thisset = {"apple", "banana", "cherry"}

# # print("banana" in thisset)




# # # ---------------loop set items-----------

# # thisset = {"apple", "banana", "cherry"}

# # for x in thisset:
# #   print(x)



# # *****************************************************************************


# # -----------------dictionary------------


# # dictionaries are used to store data values in key:value pairs.
# # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# # Dictionary items are ordered, changeable, and do not allow duplicates.
# # Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# # Dictionaries cannot have two items with the same key:


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(thisdict)

# print(thisdict["brand"])

# thisdict["year"] = 2018

# print(thisdict)

# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }

# # if "model" in thisdict:
# #     print("Yes, 'model' is one of the keys in the thisdict dictionary")
    
    
    
# # get values

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# print(x)




# # ------------looping-----------

# # for x in thisdict:
# #   print(x)
  
  
# # for x in thisdict:
# #   print(thisdict[x])
  
  
# # for x in thisdict.values():
# #   print(x)
  
  
  
# # for x in thisdict.keys():
# #   print(x)