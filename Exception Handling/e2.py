try:
    date = eval(input("enter data:"))
except SyntaxError:
    print('Invalid date entered.')
    print('please enter only integers')
else:
    print('you have entered', date)