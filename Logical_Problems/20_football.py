'''
20.Create a class that takes the following four arguments for a particular football
player:
Name, age, height, weight. Also, create three functions for the class that returns
the following strings:

get_age() ➞ "David Jones is age 25"
get_height() ➞ "David Jones is 175cm"
get_weight() ➞ "David Jones weighs 75kg"
'''

class Player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is age {self.age}"

    def get_height(self):
        return f"{self.name} is {self.height}cm"

    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"

p = Player("David Jones", 25, 175, 75)
print(p.get_age())
print(p.get_height())  
print(p.get_weight())  