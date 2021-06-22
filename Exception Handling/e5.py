try:
    x = int(input('enter a number:'))
    y = 1/x
finally:
    print('we are not catching any exception!')
    print('the inverse of {:d} is {:.2f}'.format(x, y))
