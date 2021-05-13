# Python | Program to check if a string contains any special character
import re

s = input("enter a string:")

sc = "!@#$%^&*()_+-=+{}[]\|':;<>,.?/~`"

print("method 1 using naive method")

def ch():
    for i in sc:
        if i in s:
            return True
            break
    else:
        return False

flag = ch()

if flag == True:
    print("the given string {:s} contains special char".format(s))
else:
    print("the given string {:s} does not contains any special char".format(s))

print("...........................................................")
print("method 2 using regular expression")


# Function checks if the string
# contains any special character
def run(string):
    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    # Pass the string in search
    # method of regex object.
    if (regex.search(string) == None):
        print("String is accepted")

    else:
        print("String is not accepted.")


# Driver Code

# Enter the string
string = "Geeks$For$Geeks"

# calling run function
run(string)

