import copy
import random
# a program to perform a large number of experiments 
# to estimate an approximate probability: no math!

class Hat:
  """a hat containing different balls"""
  def __init__(self, **kwargs):
    """Args: {"red": 2, "blue": 1}"""
    self.contents = []

    if(len(kwargs)==0):
      print("at least one argument needed")
      quit()

    for k,v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, num):
    """remove balls at random from contents and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement"""
    s = []
    if(num>len(self.contents)):
      return self.contents

    # random list of indices  
    tl = random.sample(range(len(self.contents)), k=num)
    for i in tl:
      s.append(self.contents[i]) # s: list based on indices

    # for: i = 0..contents.index
    # add contents[i] to tmp-array
    # but only if: i not in tl
    tmp = [self.contents[i] for i in range(len(self.contents)) if not i in tl]
    self.contents=tmp # contents without tl
    return s


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  """makes a number of experiments and returns a probability for expected_balls. probability is based on experiments, not on math"""
  expected = []
  print(expected_balls)
  for k,v in expected_balls.items():
    for i in range(v):
      expected.append(k)

  hit = 0
  for ne in range(num_experiments):
    ch = copy.deepcopy(hat)
    drawn = ch.draw(num_balls_drawn)

    chk = False
    for e in expected:
      if e in drawn:
        chk=True
        drawn.remove(e)
      else:
        chk = False
        break # failed if one element is not found in num_balls_drawn
      
    if chk:
      hit += 1
  
  return hit/num_experiments

