# example for try except

#   division by Zero exception

try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: You tried to divide by zero!")
else:
    print("The result is", result)
finally:
    print("Execution completed.")




# : Handling Multiple Exceptions


try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: You tried to divide by zero!")
else:
    print("The result is", result)
finally:
    print("Execution completed.")


#  Using except to Handle Any Exception

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("The result is", result)
finally:
    print("Execution completed.")




# program to divide two numbers


# try:
#     a = int(input("enter a number"))
#     b = int(input("enter a number"))
#     c = a/b
#     print(c)

# except:
#     print("please enter the valid input")






# try:
#     a = int(input("enter a number"))
#     b = int(input("enter a number"))
#     c = a/b
    

# except:
#     print("please enter the valid input")
    
    
# else:
#     print(c)



# --------------------------------------------------------------------------






# try:
#     a = int(input("enter a number"))
#     b = int(input("enter a number"))
#     c = a/b
    

# except:
#     print("please enter the valid input")
    
    
# else:
#     print(c)
    
# finally:
#     print('end of the program')









while True:
    try:
        a = int(input("enter a number"))
        b = int(input("enter a number"))
        c = a/b
        

    except:
        print("please enter the valid input")
        
        
    else:
        print(c)
        break
