from string import ascii_uppercase, digits
from random import choices

class Robot:
    used_names = set()

    def __init__(self):
        self.name = None
        self.reset()

    def reset(self): 
        while self.name is None or self.name in self.used_names:
            self.name = ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))
        
        self.used_names.add(self.name)

# dev tests
# r = Robot()
# print(r.name)
# print(r.reset())
# print(r.name)
