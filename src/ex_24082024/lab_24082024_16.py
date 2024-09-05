# Next Point:
# Function with Multiple Argument

def print_argument(*args):
    # *args means you can give multiple argument and any type of data type argument! There is no limit , and this is a list!
    print(args[0])  # Here 0 means, it will print first argument.


print_argument("Mudit", "Aman", "udit")         # here Mudit, Aman and udit these are argument!!
# Output: Mudit                  # As Mudit is placed at (args[0])  0th place, so it will print Mudit

print_argument("udit", "aman")
# Output: udit

# Note:
# As you are using *args then you can use multiple argument like below!
print_argument("Anupam", "Aman", "udit", 10, True, "false", "Anup")
# Output: Anupam


print_argument()                        # here you are not passing any argument!
# Output: IndexError: tuple index out of range


# What is the function type of above mentioned function ?
# Ans: It is no return type with argument function!

# ===================================================================
