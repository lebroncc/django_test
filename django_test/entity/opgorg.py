#coding=utf-8

class Opgorg(object):
  def __init__(self):
    self.id=''
    self.name=''
    self.code=''
    self.Parent = None

  def print_Opgorg(self):
    # Python 2.7 + .format优化写法
    print("{self.name}'s code is: {self.code}".format(self=self))    
