#parent class
class Person:
    def __init__(self, name, contact):
        self.name=name
        self.contact=contact
    def address(self):
        print(self.name,self.contact)
        
        
#child class
class Doctor(Person):
    pass
class Patient(Person):
    pass

d1=Doctor("Raj","9876543210")
d2=Doctor("ravi","9656738289")
d1.address()
d2.address()

p1=Patient("ram","345678987")
p2=Patient("allu","998748393")
p3=Patient("inji","039030290")
p4=Patient("kunji","909390290")

p1.address()
p2.address()
p3.address()
p4.address()