## convert celsius to farenheit
def C_to_F(Celsius):
      
  Fahrenheit = 9.0/5.0 * Celsius + 32

  return Fahrenheit #The return statement causes your function to exit 
#and hand back a value

Celsius = int(input("Enter  temperature in Celsius: ")) #use raw_input instead of input  
print(C_to_F(Celsius))


# farenehit to celsius 
def F_to_C(F):
    
    Celsius = (F - 32) * 5.0/9.0

    print(Celsius)

F = float( input("Enter temperature in Farenheitt: ") )
F_to_C(F)   


