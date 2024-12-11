class Student:
    def _init_(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number

    def get_details(self):
        print(f"Student Name: {self.name}")
        print(f"Student Roll_number: {self.roll_number}")

class Marks(Student):
    def _init_(self,name,roll_number):
        super()._init_(name,roll_number)
        self.Marks=[]

    def get_Marks(self):
        n=int(input("Enter the number of subject: "))
        print("Enter the marks for the subject: ")
        for  i in range(n):
            Marks=float(input(f"Subject {i+1}: "))
            self.Marks.append(Marks)

    def Calculate_and_Percentage(self):
        total=sum(self.Marks)
        percentage=total / len(self.Marks)
        print(f"Total Marks : {total}")
        print(f"Percentage : {percentage}")
name= input("Enter your Name : ")
roll_number=int(input("Enter your roll_number : "))

student = Marks(name,roll_number)
student.get_details()
student.get_Marks()
student.Calculate_and_Percentage()
