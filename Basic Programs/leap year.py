# program to find if the given year is leap year or not

def is_leap(y):
    if (((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0)):
        print("{} is leap year".format(y))
    else:
        print("{} is not leap year".format(y))



year = int(input("enter a year:"))

is_leap(year)
