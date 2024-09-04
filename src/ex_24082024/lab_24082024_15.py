# Example:
def sum_of_three_numbers(a=10, b=25, c=15):  # Here a, b, c mentioned as default
    return a + b + c


result = sum_of_three_numbers(c=15, a=25, b=10)  # Here you have changed the argument order.
print(result)


# Output: 50

# ==============================================================

# Next Example:
def sum_of_three_numbers(a=10, b=25, c=15):  # Here a, b, c mentioned as default
    return a + b + c


result2 = sum_of_three_numbers(c=15, a=25)  # Here you have changed the argument order.
print(result2)
# Output: 65

# ==============================================================
