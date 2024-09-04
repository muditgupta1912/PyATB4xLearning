# Calling a function inside another function!!

def greet_to_all_of_you():
    print("Hello All")

def greet():
    print("Hi")
    greet_to_all_of_you()

#Here we are calling greet() function !!
greet()



