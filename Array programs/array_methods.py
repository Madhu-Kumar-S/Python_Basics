# array methods
import array

elements = [1, 2, 3, 4, 5]  # iterable object
a = array.array('i', elements)  # defining array
print(*a)
print(a.typecode)  # returns the type code char of an array
print(a.itemsize)  # returns the size of an items stored in array in bytes

a.append(6)  # adds the element at end of an array
print(*a)

print(a.count(5))  # returns the repetition of an element

a.extend([7, 8])  # extends the element or any iterable object at end
print(*a)

a.fromlist([9, 10])  # adds list at end
print(*a)

print(a.index(1))  # returns the element associated with that position

a.insert(9, 11)  # inserts the element at a given position
print(*a)

a.pop()  # removes the last element
print(*a)

a.remove(9)  # removes the particular element
print(*a)

a.reverse()  # reverses the entire array
print(*a)

print(a.tolist())  # converts array to list