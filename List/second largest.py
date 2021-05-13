# python program to find second largest element in list

lst = eval(input("enter a list:"))
print(lst)

def sl(l):
    t = l.copy()
    t.remove(max(t))
    print("second largest element in list is {}".format(max(t)))

sl(lst)