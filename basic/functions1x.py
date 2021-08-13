def print_box(message):
    n=len(message)
    print("*" * n )
    print (message)
    print( "*" * n )

print_box("Hello World!")
print()
print_box("Enter a word:")
word = input()

if word == 'python':
    print_box("You entered Python!")
else:
    print_box("You didn't enter Python :(")
