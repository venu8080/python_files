class Student:
    def _init_(self, name, roll_no):
        # 1. instance variables created inside constructor using self
        self.name = name
        self.roll_no = roll_no
        print("Inside Constructor:")
        print("Name:", self.name)
        print("Roll number:", self.roll_no)

    def update_marks(self, marks):
        # 2. instance variable created/modified inside instance method using self
        self.marks = marks
        print("\nInside Instance Method:")
        print(f"{self.name}'s Marks updated to:", self.marks)


# Example usage:
s1 = Student("Manesh", 101)
s1.update_marks(95)

