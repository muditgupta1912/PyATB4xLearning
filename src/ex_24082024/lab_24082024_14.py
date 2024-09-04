# Example:

def sum_of_numbers(a, b):
    return a + b


result_of_sum = sum_of_numbers(10, 40)
print(result_of_sum)
# Output: 50

result_of_sum2 = sum_of_numbers(a=140, b=120)
print(result_of_sum2)


# Output: 260

# ==========================================================================

# Example:

def sum_of_three_numbers(a, b, c=15):
    return a + b + c


result = sum_of_three_numbers(25, 35)  # Here c= 15 taking as default
print(result)


# Output: 75

# ==========================================================================

# Example:
def sum_of_three_numbers(a=10, b=25, c=15):  # Here a, b, c mentioned as default
    return a + b + c


result = sum_of_three_numbers()         # Here a, b, c taking as default
print(result)
# Output: 50

# ==========================================================================
