#class anak diluar,yg didalam kurung kelas induk
class Person:
 def __init__(self,name, gender, age):
    self.name = name
    self.gender = gender
    self.age = age

 def talking():
  pass
 def walking():
  pass
 def sleep():
  pass

class Student(Person):
  def __init__(self, name, gender, age, BirthYear):
   super().__init__(name, gender,age)
   self.BirthYear = BirthYear

def belajar():

 
 x = Student('Aqul', 'men', 20, 2005)
 print(x.name)
 print(x.BirthYear)
 



 

 class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)