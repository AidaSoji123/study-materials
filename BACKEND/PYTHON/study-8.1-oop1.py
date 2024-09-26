# ####------OOPS------####

# class Cars:
#     def __init__(self,name,model,price,color):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.color = color
#  #method of class cars   
#     def start(self):
#         print(self.name + " engine Started")
#         print(self.model +" is a highly rare model")
#         print(str(self.price) +" is the price")
#         print(self.color +" is the color")

# #crate objects with class cars     
# car1=Cars("swift","Zxi",900000,"white")
# car2=Cars("polo","gt",1000000,"red")
# car3=Cars("crysta","zxi",2600000,"black")
# car1.start()

# #print object details one by one

# print("My first Cars object is " + car1.name + " the model is "+ car1.model +" the price of the car with this model is " + str(car1.price) +" and the color of the car is " + car1.color)
# print("My first Cars object is " + car2.name + " the model is "+ car2.model +" the price of the car with this model is " + str(car2.price) +" and the color of the car is " + car2.color)
# print("My first Cars object is " + car3.name + " the model is "+ car3.model +" the price of the car with this model is " + str(car3.price) +" and the color of the car is " + car3.color)





# -----------------------------------------oop using loop----------------------------------------------------------------


# # Create a student class with properties name,dob,gender,course,ph_no, course completed status and a method of eligibility to attend interviews

# class Student:
#     def __init__(self,name,dob,gender,course,ph_no,course_completed):
#         self.name = name
#         self.dob = dob
#         self.gender = gender
#         self.course = course
#         self.ph_no = ph_no
#         self.course_completed = course_completed
#         # self.interview_eligible = interview_eligible
        
#     def eligibility(self):
#         if self.course_completed == True:
#             # self.interview_eligible = True
#             print(self.name + " is eligible for interview")
#         else:
#             # self.interview_eligible = False
#             print(self.name + " is not eligible for interview")
                
# #create objectwith class students
# std1 = Student("vijay","21-09-1995","male","BBA",9654567837,True)
# std2 = Student("surya","1-11-2004","male","12th",9876567837,False)
# std3 = Student("ajith","31-02-1975","male","MBBS",9989387837,True)

# # #looping the class objects
# studentList= [std1,std2,std3]
# for std in studentList :
#     print(std.name)
#     print(std.dob)
#     print(std.gender)
#     print(std.course)
#     print(std.ph_no)
#     print(std.course_completed)
#     std.eligibility()
  
