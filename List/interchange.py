# Python program to interchange first and last elements in a list

def interchange(l):
    l[0], l[-1] = l[-1] , l[0]

    print("interchanged list is {}".format(l))

lst = [1, 2, 3, 4, 5]

print("original list is {}".format(lst))
interchange(lst)