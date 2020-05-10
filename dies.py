from random import randint
class Dies():
    def __init__(self,die_count=8):
        self.die_count=die_count
    def finalroll(self):
        return randint(1,self.die_count)
