# Aim:- Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. The Student class has data members such as those representing rollNumber, Name, etc. Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects. Derive Result from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this relationship.
# Name:- Meghal Shah
# ID:- 20CS085

class Student:
    def __init__(self,rollno,name,division):
        self.name=name
        self.rollno=rollno
        self.divison=division
    def getStudent(self):
        print("Name : ",self.name)
        print("Roll No : ",self.rollno)
        print("Division : ",self.divison)

class Exam(Student):


    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

class Result(Exam):

    def getTotalMarks(self):
        Total_Marks=sum(self.getMarks())
        return Total_Marks


Exam=Result(10,"Andrew",2)
print("\n---- Student Information ---- \n")
Exam.getStudent()
Exam.setMarks([15,25,35,45,55,65])
print("Total Marks :- ",Exam.getTotalMarks())
