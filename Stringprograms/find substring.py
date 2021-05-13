# Python | Check if a Substring is Present in a Given String
import re
main_string = input("enter a main string:")

sub_string = input("enter a sub string:")

print("method 1")
if sub_string in main_string:
    print("{:s} is found in {:s}".format(sub_string, main_string))
else:
    print("{:s} is not found in {:s}".format(sub_string, main_string))

print("method 2")
if re.search(sub_string, main_string):
    print("{:s} is found in {:s}".format(sub_string, main_string))
else:
    print("{:s} is not found in {:s}".format(sub_string, main_string))

print("method 3")
if main_string.count(sub_string) > 0:
    print("{:s} is found in {:s}".format(sub_string, main_string))
else:
    print("{:s} is not found in {:s}".format(sub_string, main_string))

print("method 4")
if main_string.find(sub_string) != -1 :
    print("{:s} is found in {:s}".format(sub_string, main_string))
else:
    print("{:s} is not found in {:s}".format(sub_string, main_string))
