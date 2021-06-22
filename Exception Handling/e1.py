# an exception example
# open a file
try:
    f = open("myfile", "w")
    print('File opened')
    a, b = [int(i) for i in input("enter values of a and b:").split()]
    c = a / b
    f.write("writing {:f} into myfile".format(c))
except ZeroDivisionError:
    print('division by zero is not possible!')
    print('please do not enter 0 in input.')
else:
    print('successfully writen in file.')
# close the file
finally:
    f.close()
    print('File closed')
