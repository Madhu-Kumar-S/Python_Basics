# Selection sort using array array
import array

print("................Selection Sort...............")
elements = [int(x) for x in input("enter the elements:").split()]
arr = array.array('i', elements)
print("array is:", *elements)


def ss_sort(a):
    n = len(a)
    for i in range(n):
        min_pos = i
        for j in range(i+1, n):
            if a[min_pos] > a[j]:
                min_pos = j
        a[i], a[min_pos] = a[min_pos], a[i]
    return a


result = ss_sort(arr)
print("Sorted array: ", *result)
