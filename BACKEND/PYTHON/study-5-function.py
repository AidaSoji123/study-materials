# def my_function():
#   print("Hello from a function")
 
  
# my_function()
# my_function()



# ------------------

# def my_function(fname):
#   print(fname + " reached")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# ---------------------------

# If the number of arguments is unknown, add a * before the parameter name:

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")


# ---------------------------------

# If the number of keyword arguments is unknown, add a double ** before the parameter name:

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# -------------default argument---------------

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")




# --------------------------list as an argument------------

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# --------------------return value--------------

# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))