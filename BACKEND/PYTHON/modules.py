# function to display hello name
def greeting(name):
  print("Hello, " + name)
  
#   function to find the entered number is negative or positive

def is_positive(num):
  if num > 0:
    print("Positive")
  else:
    print("Negative")
    
    
# function to find the entered number is prime or not

def is_prime(num):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        print(num, "is not a prime number")
        break
    else:
        print(num, "is a prime number")
        

    
          