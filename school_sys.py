
class Course:
    def __init__(self, cname, max_student):
        self.cname=cname
        self.max=max_student

class Student:
    def __init__(self, name, rollno ):
        self.name=name
        self.rollno=rollno
        self.courses=[]

    def enroll(self, course):
        self.courses.append(course)
    

    def show_course(self):
        print(f"{self.name}(Rollno: {self.rollno}) is enroll in course: ", end="")

        for i, course in enumerate(self.courses):
            if i==len(self.courses)-1:
                print(course.cname)
            else:
                print(course.cname, end=", ")    


def main():
    
    sname=input("Student name: ")
    s_rollno=int(input("Roll number: "))
    stud=Student(sname,s_rollno)

    math=Course("Advance Mathemetics",35)
    english=Course("English",35)
    hindi=Course("Hindi",35)
    phy=Course("Physics",30)
    chem=Course("Chemestry",30)
    comp=Course("Computer",25)

    stud.enroll(english)
    stud.enroll(comp)
    stud.enroll(math)
    stud.enroll(hindi)
    stud.enroll(chem)
    print("Student enroll detail...")
    stud.show_course()


if __name__=="__main__":
    main()