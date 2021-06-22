# The assertion statement
# syntax : assert condition, message

try:
    x = int(input("enter a integer value greater than 0 and less than 10:"))
    assert ((x > 0) and (x < 10)), 'Your input is incorrect'
except AssertionError as a:
    print('error =', a)
