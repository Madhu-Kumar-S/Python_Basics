# Python | Reversing a List

def rev(l):
    print("method 1 using reverse function:")
    l.reverse()
    print(l)
    l.reverse()
    print("method 2 using slicing")
    print(l[::-1])

lst = [1, 2, 3, 4, 5]
print("before reversing")
print(lst)
print("after reversing")
rev(lst)