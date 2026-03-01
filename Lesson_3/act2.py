class Student:
    grade = 10
    name = "Penguin"

    def introduction(self):
        print("Hi, I m a student")

    def details(self):
        print("My name is : ", self.name)
        print("My Grade is ", self.grade)

obj1 = Student()
obj1.introduction()
obj1.details()