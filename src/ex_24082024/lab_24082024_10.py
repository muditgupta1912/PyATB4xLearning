# To print name in upper case letters.
# Example:
def hello_to_all_from(name="Mudit"):
    print("Hello to all from", name.upper())  # this will make upper case letters.


hello_to_all_from()
hello_to_all_from("amit")
hello_to_all_from(name="vivek")


# Output:
# Hello to all from MUDIT
# Hello to all from AMIT
# Hello to all from VIVEK


# ================================================================================

# To pass multiple Arguments.

# Example1:
def multiple_arguments(name1="Mudit", name2="Amit", name3="Ram"):
    print("Hello", name1, name2, name3)

multiple_arguments()
# output: Hello Mudit Amit Ram


# Example2:
def multiple_args(name1="Arpita", name2="Pramod", name3="Amit"):
    print("Multiple Arguments", name1, name2, name3)


multiple_args(name1="Ram", name2="Yunus", name3="Deepshikha")
# Output = Multiple Arguments Ram Yunus Deepshikha


# Example3:
def multiple_args(name1="Arpita", name2="Pramod", name3="Amit"):
    print("Multiple Arguments", name1, name2, name3)


multiple_args(name1="PRAMOD")
# Output = Multiple Arguments PRAMOD Pramod Amit
# Here name1="PRAMOD" and rest were taken as default.


