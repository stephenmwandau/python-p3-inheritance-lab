from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = []
    
    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)

my_student = Student("My", "Student")
my_student.learn("Decorators in python")