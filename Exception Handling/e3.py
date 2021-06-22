try:
    name = input('enter filename:')
    f = open(name, 'r')
except FileNotFoundError:
    print('file not found:{:s}'.format(name))
    print('please enter correct file name')
else:
    n = len(f.readlines())
    print(name, 'has', n, 'lines')
    f.close()
