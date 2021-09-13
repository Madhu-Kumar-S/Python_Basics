# program to display all positions of a substring in a given main string.

main_string = input("enter main string:")
sub_string = input("enter sub string:")

flag = False
pos = -1

while True:
    pos = main_string.find(sub_string, pos+1, len(main_string))
    if pos == -1:
        break
    else:
        print("element {:s} found at position {:d}".format(sub_string, pos + 1))
        flag = True

if not flag:
    print("substring not found")