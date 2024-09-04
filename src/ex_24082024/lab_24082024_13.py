# Create a program to sum of three number from user input !

num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
num3 = int(input("Enter number 3"))


def sum_of_three_numbers(n1, n2, n3):  # Note: while definition, variable name can be anything!
    return n1 + n2 + n3


result = sum_of_three_numbers(num1, num2, num3)
print(result)
# Output: 60

# =========================================================

# Same above example in different way.
# Example:

num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
num3 = int(input("Enter number 3"))


def sum_of_three_numbers(n1, n2, n3):        # Note: while definition, variable name can be anything!
    return n1 + n2 + n3


result = sum_of_three_numbers(n1= num1, n2=num2, n3=num3)
print(result)
# Output: 90

# =========================================================
