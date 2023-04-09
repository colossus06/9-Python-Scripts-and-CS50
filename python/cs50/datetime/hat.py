import random

class Hat:
    def __init__(self):
        self.houses=["erz","huk","dem"]

    def sort(self, name):
        house= random.choice(self.houses)
        print(name, "is in", house)



hat=Hat()
hat.sort("Harry")