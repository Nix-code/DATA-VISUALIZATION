"""pygal makes projects fit in every device you are working on"""
from random import randint
"""create class for single die"""
class Die():
    def __init__(self,num_die=6):
        #six sides sie
        self.num_die=num_die
    def roll_me(self):
        """return the randint value ,it chooses the random values """
        return randint(1,self.num_die)
        
