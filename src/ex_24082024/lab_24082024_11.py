# Next 4th Function type:
# Argument and Return type function:

# Example:
def sum_of_two_number(num1, num2):      # here Argument is num1 and num2
    return num1 + num2                  # here this return  is  Return type function


result = sum_of_two_number(10 , 20)
print(result)
# Output: 30

# =============================================================

# Example:
# Same above example in different way.
def sum_of_two_number(num1, num2, num3):
    return num1+num2+num3


result = sum_of_two_number(num1 = 10, num2 = 30, num3 = 40)  # This is known positional argument passing.
print(result)
# output = 80

# =============================================================

# Same above example, if we dont pass positional argument !
# Example:

def sum_of_two_numbers(num1, num2):
    return num1 + num2


result = sum_of_two_numbers()           # This will show error as we are not passing positional arguments.
print(result)
# Output: TypeError: sum_of_two_numbers() missing 2 required positional arguments: 'num1' and 'num2'

# =============================================================
