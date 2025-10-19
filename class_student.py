class Student:
    school_name="ABC School"
    def __init__(self,name):
        self.name=name
        @classmethod
        def change_school(cls,new_name):
         scls.school_name=new_name
        Student.change_school("XYZ School")
        print(Student.school_name)
