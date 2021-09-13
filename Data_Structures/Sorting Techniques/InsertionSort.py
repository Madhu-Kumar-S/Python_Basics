# Insertion sort using array array
import array

print("................Insertion Sort...............")
elements = [int(x) for x in input("enter the elements:").split()]
arr = array.array('i', elements)
print("array is:", *elements)


def is_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j = j-1
        else:
            a[j+1] = key
    print("Sorted array is: ", *a)


is_sort(arr)
