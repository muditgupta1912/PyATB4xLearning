# user of OR operator with match keyword!!

#Example:
user_input = input("Enter the user type admin, guest, manager\n ")
match user_input:
    case "admin" | "guest":
        print("Hello admin")
    case "manager":
        print("Hello Manager Sir")
    case _:
        print("May I know you ?")
