# if you don't define __init__ initiated values are inherited from the parent class.
class Animal:
    def __init__(self):
        self.species = None
        
class Monkey(Animal):
    pass

monkey = Monkey()
print(monkey.species) # this will print None


class Human(Animal):
    def __init__(self):
        self.species = 'Human'
        
human = Human() 
print(human.species) # this will print Human