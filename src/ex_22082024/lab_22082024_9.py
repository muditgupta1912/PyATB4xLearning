## Write a programme to ask user, which browser he wants to use!!
browser_name = input("Enter Browser Name\n")
browser_name = browser_name.lower()
#Here using this "browser_name.lower()", if user will enter browser name in capital letters,
# it will take them in small letters.
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