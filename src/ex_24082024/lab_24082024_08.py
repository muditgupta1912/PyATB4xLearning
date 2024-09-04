# # Next Topic:
# There are 4 types of user defined functions.
# 1. no return = These Functions can not return anything.
# 2.



## 1 Type functions:
# # NO Return type functions.
## This is also known as No Return Type and No parameters OR NO Argument .
# Example:
def greet():
    print("Hello")
result = greet()
print(result)
#Output is = None
#Here output is None and we did not pass any argument. So it is No Return Type and No parameters OR NO Argument.

#==================================================================================

### 2 Type functions:
## NO Return type with argument.
#Example:

def greet_by_name(name):        #Here name is a argument, we are passing 1 argument as name 
    print("Hello", name)

greet_by_name("Mudit")
#Output: Hello Mudit
