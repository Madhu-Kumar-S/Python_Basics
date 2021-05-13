# Python – Convert Snake case to Pascal case

str = input("enter the string:")

print("original string is:",str)

str = str.replace('_', ' ')

str = str.title()
print("after case convertion:",str)