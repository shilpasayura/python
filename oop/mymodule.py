#mymodule.py
import sys

class Mathx:
    PI= 22/7
    name = ""

    def __init__(self,name):
        self.name = name
        
    def add(self,x ,y):
        z=x+y
        return z
    
    def circlearea(self,r):
        a=self.PI * r * r
        return a

def multi(x,y):
    return x*y

sys.path.append(".")



