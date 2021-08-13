##strings in python

str1="Hello. I have a cat."

print(str1)

print (type(str1))

str2="8"

print(type(str2))

str3="She is a shot-hair"

##concatenate
print(str1+str3)

#space between strings
print(str1 + " " + str3)

c=" ".join([str1,str3])
print(c)

##string operations

#how long is my string
print (len(str1)) 

#print  first letter of str1
print(str1[0])
print(str1[-20])

#isolate hello
str1="Hello. I have a cat."

 #start index to end-1
print(str1[0:5])


#from letter at index 7 to end
print(str1[7:]) 

#from letter at index 0 to end index-1
print(str1[:7]) 


hi=str1[0:5]
print(hi)

#convert all to upper cases. Function .lower() will do the opposite

print(hi.upper()) 

str1a=str1[:] #copy a string

print(str1a)

#split according to white space
print(str1a.split()) 

print(str1a.replace('cat','black cat')) #replace cat of str1a with black cat


