
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



m=Mathx("M")

z=m.add(3,2)
print(z)

print(m.add(4,5))
print(m.add(6,11))
print(m.circlearea(7))
