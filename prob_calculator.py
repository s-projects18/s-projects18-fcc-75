import copy
import random
# a program to perform a large number of experiments 
# to estimate an approximate probability: no math!


class Hat:
  def __init__(self, **kwargs):
    """Args: {"red": 2, "blue": 1}"""
    self.contents = kwargs
    if(len(self.contents)==0):
      print("at least one argument needed")
      quit()

  def draw(self, num):
    """remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement"""
    cp = copy.deepcopy(self.contents)
    if(num>len(cp)):
      return cp
    r = []
    for i in range(num):
      pass


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pass
