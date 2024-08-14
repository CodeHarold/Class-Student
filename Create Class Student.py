class Person:
  def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

  def printname(self):
      print(self.firstname, self.lastname)

      
class Student(Person):
    def __init__(self, fname, lname, depm,):
        self.firstname = fname
        self.lastname = lname
        self.department = depm

    def printname(self):
         print(self.firstname, self.lastname, self.department)
    


class staff(Person):
    def __init__(self, fname, lname, desig,):
        self.firstname = fname
        self.lastname = lname
        self.designation = desig

    def printname(self):
         print(self.firstname, self.lastname,self.designation)

x = Student ('Harold', 'Murillo','IT')
x.printname()
y = staff('Steven', 'Mateus','designation')
y.printname()
