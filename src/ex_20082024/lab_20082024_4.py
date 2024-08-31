# Problem to find max number between three numbers

num1 = float(input("Enter num1\n"))
num2 = float(input("Enter num2\n"))
num3 = float(input("Enter num3\n"))
if num1 > num2 and num1 > num3:
    print("Max is", num1)
elif num2 > num1 and num2 > num3:
    print("Max is", num2)
else:
    print("Max is", num3)
