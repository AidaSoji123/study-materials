# # ###---ARITHMETIC OPERATORS----###

# # #ADDITION

x = 5
y = 3
print(x + y)


# #SUBTRACTION

print(x - y)

# #MULTIPLICATION
print(x * y)

# #DIVISION
print(x / y)  

# #MODULUS
print(x % y)

# #FLOOR DIVISION
print(x // y)

# #EXPONENTS
print(x ** y) #same as 2*2*2*2*2


# # ###---ASSIGNMENT OPERATORS----###

x = 5
print(x)
x += 3      # x = x +3
print("x+=3 : ",x)

x -= 3
print("x-=3 : ",x)
x *= 3
print("x*=3 : ",x)
x /= 3
print("x/=3 : ",x)
x %= 3
print("x%=3 : ",x)

x //= 3

print("x//=3 : ",x)

x=10
print("x = ",x)

x **= 3
print("x**=3 : ",x)
x = 6
x &= 3
print("x&=3 : ",x)
 


###---LOGICAL OPERATORS----###

# AND OPERATOR

print(True and False)

# OR OPERATOR

print(True or False)

# NOT OPERATOR

print(not True)

# AND OPERATOR with multiple conditions

print(True and False and True)
print(True and False and False)

# OR OPERATOR with multiple conditions

print(True or False or True)
print(True or False or False)

# XOR OPERATOR

print(True ^ False)
print(True ^ True)
print(False ^ False)

# IDENTITY OPERATOR

print(True is True)
print(True is False)
print(True is not False)

# MEMBERSHIP OPERATOR

print(True in [1, 2, 3])
print(4 in [1, 2, 3])

# IS NOT OPERATOR

print(True is not False)
print(False is not False)




###---COMPARISON OPERATORS----###

# greater than

print(5 > 3)

# less than

print(5 < 3)

# equal to

print(5 == 3)

# not equal to

print(5 != 3)

# greater than or equal to

print(5 >= 3)

# less than or equal to

print(5 <= 3)
