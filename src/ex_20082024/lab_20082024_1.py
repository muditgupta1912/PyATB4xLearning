# If else loop concept !

#Syntax
# if condition:
#    code you want to execute if condition is ture
# else:
#     code you want to execute if conditio is false

## Write a program to take user age as input and let him know, if he can go to club or not

# Create logic building
#Step1: Take user input as age, and its data type will be int
#       What will be the output datatype. It will be string


#Step2: Create rough logic
# age => 25 then print 'can go to club'
# age < 25 then print 'can not go to club'


# Step3: Write the code or logic

# So here is the programme.

age = int(input("Enter your age"))
if age >= 25:
    print("Can go to Club")
else:
    print("Can not go to club")


#Next way to do the same:
age = int(input("Enter your age"))
if age >= 25:
    print(f"Can go to Club at age {age}")
else:
    print(f"Can not go to club at age {age}")




