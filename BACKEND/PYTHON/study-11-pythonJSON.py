# ---PYTHON JSON-------------

# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.



#  using JSON loads() JSON can covert to python dictionary

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'   # its a json string

# parse x:
y = json.loads(x)

print(y)      # python dictionary

# the result is a Python dictionary:
print(y["age"])






# Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)





# JAVASCRIPT OBJECT NOTATION

# it s a format for transfering data from server to app and app to server

# import json
# x = '{"name": "Kevin","age":25}'   #  string to json

# y = json.loads(x)
# print(y)





import json
s = {"name": "Kevin","age":25}

r = json.dumps(s)
print(r)