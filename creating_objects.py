class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
        def dispaly_info(self):
            return f"Name: {self.name},Marks; {self,marks}"
        s1 = Student("Manesh",99)
        s2 = Student("manesh",100)
        print(s1.display_info())
        print(s2.display_info())
