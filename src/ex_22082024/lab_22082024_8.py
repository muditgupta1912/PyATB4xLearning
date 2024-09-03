# Next Topic:
# Match Statement = Match statement is known as switch in Java.
# Match statement means, match the output and execute.

#Syntax of Match:

match variable:
    case pattern1:
        # execute code block
    case pattern2:
        # execute code block


## Write a programme to ask user, which browser he wants to use!!
browser_name = input("Enter Browser Name\n")
match browser_name:
    case "firefox":
        print("Firefox code executed")
    case "chrome":
        print("chrome code executed")
    case "safari":
        print("safari code executed")
    case "edge":
        print("edge code executed")
    case _:
    # Here underscore means default, if it does not find anything.
        print("Browser Not Found")



