def ask_name():
    name = input("Enter your name: ")
    return name

def get_greeting(name):
    return "Hello " + name


print(get_greeting(ask_name()))

