class Student:
        name="ROSHNI"
        roll_no=1519
        address="Mumbai"
        college="S.H.Jondhale"
        age=20
class Details(Student):
        def display(self):
                print("Name =",self.name)
                print("Roll NO =",self.roll_no)
                print("Address =",self.address)
                print("College =",self.college)
                print("Age =",self.age)
stud=Details()
stud.display()
