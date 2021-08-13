## convert celsius to farenheit
def C_to_F(Celsius):
      
  Fahrenheit = 9.0/5.0 * Celsius + 32
#The return statement causes your function to exit 
#and hand back a value
  return Fahrenheit 
  
print(C_to_F(9))

def area_circle(radius):
    pi=3.14
     #no need to declare an additional variable 
    return pi * radius ** 2

print(area_circle(2))

#multiple input parameters
def volume(radius, height):  
    pi = 3.14159
    v=pi * radius ** 2 * height
    return v

print ("volume of cylinder with radius", 1, "and height 2 is", volume(1,2))
