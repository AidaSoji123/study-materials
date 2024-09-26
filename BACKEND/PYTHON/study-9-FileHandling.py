#  file Handling

# 1. open()
# 2. read()
# 3. close()
# 4. write()
# 5. append()


##---Python file handling---##

##->METHOD 1<-##
# open a file
f = open("myfile.txt", "r")

# read the file
print(f.read())

# close the file
f.close()

##->METHOD 2<-##
# open a file
f = open("myfile.txt", "r")

# read the file
print(f.readline())

# close the file
f.close()

##<-METHOD 3->##
# open a file
f = open("myfile.txt", "r")

# read the file
for x in f:
    print(x)

# close the file
f.close()

##<-METHOD 4->##
# append the file

f = open("myfile.txt", "a")
f.write("\nThis is the fourth line")

# close the file
f.close()

