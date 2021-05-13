# Python Program for array rotation

from array import *

arr = array('i',[1,2,3,4,5])
print("original array is {}".format(arr))

ip1 = input("enter 'l' left rotation or 'r' right rotation:")

ip2 = int(input("enter how many times to rotate:"))

def rotation(ch, ro, a):

    if ch == 'l':
        for i in range(ro):
            t = a[0]
            a.remove(a[0])
            a.append(t)
        print("array after left rotation is {} ".format(a))

    elif ch == 'r':
        for i in range(ro):
            t = a[-1]
            a.remove(a[-1])
            a.insert(i, t)
        print("array after right rotation is {} ".format(a))

    else:
        print("invalid input")


rotation(ip1, ip2, arr)

