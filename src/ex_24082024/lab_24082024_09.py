# ## 3 Type functions:
# # NO Return type with default argument.
# # default argument means that if you dont pass anything then default value will be taken.
# Example:

def hello_to_default_arg(name = "Mudit"):  # here you have passed default argument as name = "Mudit"
    print("Hello", name)


hello_to_default_arg()          # here you are calling function without passing anything.
# Output: Hello Mudit            # because you are calling function without passing anything.
# So it took default argument as name = "Mudit"

# ====================================================================================

# Next Example:
def hello_to_default_arg(name = "Mudit"):    # here you have passed default argument as name = "Mudit"
    print("Hello", name)


hello_to_default_arg("Vivek")       # here you are calling function with  passing something.
# Output: Hello Vivek               # because you are calling function with  passing something. So it took that value.

# ====================================================================================

# Next Example:

def hello_to_default_name(name = "Mudit"):
    print("Hello", name)


hello_to_default_arg(name = "Tushar")   # This is known positional argument passing.
# Output: Hello Tushar               # because you are calling function with  passing something. So it took that value.


# ====================================================================================

