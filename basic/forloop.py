
#This is a dictionary

dict={'Japan':'Tokyo', 'China':'Beijing','Taiwan':'Tapei','South Korea':'Seoul'}

for i in dict:
    print(i)



for k,v in dict.items():
    print (k, "capital city", v)

for i in dict:
    print (i,dict[i])  

for i in range(21):
    if i % 2 == 0:
        print(i)  