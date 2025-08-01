class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

# Create an object
student1 = Student("Alice", "A")
student1.display()

student2 = Student("Ann", "B")
student2.display()

Student3 = Student("Boby", "A")
Student3.display()

class Consumer:
    def __init__(self, name, gender, income):
        self.name = name
        self.gender = gender
        self.income = income

    def display(self):
        print(f"Name: {self.name}, Gender: {self.gender}, Income: ₹ {self.income}")

# Create an objects
consumer1 = Consumer("Alice", "Female", 45000)
consumer2 = Consumer("Ann", "Female", 25000)
consumer3 = Consumer("Boby", "Male", 15000)
consumer4 = Consumer("Bibin", "Male", 50000)

consumer1.display()
consumer2.display()
consumer3.display()
consumer4.display()