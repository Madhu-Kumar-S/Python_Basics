# Python program to Find the size of a Tuple

import sys

t1 = (1, 2, 3, 4, 5)
t2 = ("madhu", "kumar")
t3 = (1.2, 2.3, 3.4)

# 1.Using getsizeof() function:
# The sys.getsizeof() function includes the marginal space usage, which includes
# the garbage collection overhead for the object. Meaning it returns the total space occupied by the
# object in addition to the garbage collection overhead for the spaces being used.
print("size of tuple t1 = {} is : {} bytes".format(t1, sys.getsizeof(t1)))
print("size of tuple t2 = {} is : {} bytes".format(t2, sys.getsizeof(t2)))
print("size of tuple t3 = {} is : {} bytes".format(t3, sys.getsizeof(t3)))

# 2.Using inbuilt __sizeof__() method:
# Python also has an inbuilt __sizeof__() method to determine the space allocation
# of an object without any additional garbage value. It has been implemented in the below example.
print("size of tuple t1 = {} is : {} bytes".format(t1, t1.__sizeof__()))
print("size of tuple t2 = {} is : {} bytes".format(t2, t2.__sizeof__()))
print("size of tuple t3 = {} is : {} bytes".format(t3, t3.__sizeof__()))