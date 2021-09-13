# linear search / Sequential Search using array

import array

print(".............Linear search............")
elements = [int(x) for x in input("Enter the elements: ").split()]
arr = array.array('i', elements)
print("array is: ", *arr)
element = int(input("Enter an element to search: "))

flag = False
for i in range(len(arr)):
    if arr[i] == element:
        print("Element found at position ", i+1)
        flag = True

if not flag:
    print("Element not found")
