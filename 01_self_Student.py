class Student:
  def __init__(self,name,marks):
        self.name =name
        self.marks=marks
  def disply (self):
    print(f"Name:{self.name},marks:{self.marks}")     
s1=Student("Samina",90) 
print(s1.marks)  
s1.disply()   
    