
# Previous example with passing default argument !
# Example:
def sum_of_two_numbers(num1 = 10, num2 = 20):  # here you have passed (num1 = 10, num2 = 20) as default argument
    return num1 + num2


result = sum_of_two_numbers()  # As you have mentioned default argument above, so if you will not mention here, it not impact.
print(result)
# Output: 30

# ==========================================================================

# Example:
def sum_of_two_number(num1 = 10, num2 = 20):   # here you have passed (num1 = 10, num2 = 20) as default argument
    return num1 + num2


result = sum_of_two_numbers(num1= 100, num2= 200) # As you have mentioned default argument above, but you have passed positional argument here, so it will replace.
print(result)
# Output: 300


