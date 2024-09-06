#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
    ]

    def teach(self, min_index = 0, max_index = None):
        '''teaches from list of knowledge.'''
        if not self.knowledge:
            return "No knowledge to teach."
        
        if max_index is None:
            max_index = len(self.knowledge) - 1
        
        min_index = max(min_index, 0)
        max_index = min(max_index, len(self.knowledge) - 1)
        
        if min_index > max_index:
            return "Invalid index range."

        random_index = random.randint(min_index, max_index)
        
        print(f"Random knowledge: {self.knowledge[random_index]}")
        return self.knowledge[random_index]


my_teacher = Teacher("My", "Teacher")
my_teacher.teach()