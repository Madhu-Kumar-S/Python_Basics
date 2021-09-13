# Binary search using array

import array

print(".................Binary Search..................")
elements = [int(x) for x in input("Enter elements: ").split()]
elements = array.array('i', elements)
print("Array is: ", *elements)
n = len(elements)


def ss_sort(a):  # selection sort or can use inbuilt sort method to sort an array
    for i in range(n):
        min_pos = i
        for j in range(i+1, n):
            if a[min_pos] > a[j]:
                min_pos = j
        a[i], a[min_pos] = a[min_pos], a[i]
    return a


# or we can use inbuilt function arr  = sorted(arr)
sort_arr = ss_sort(elements)
print("Sorted array is:", *elements)

search_element = int(input("Enter an element to search: "))


def bs(arr, element, tl):
    low = 0
    high = tl-1
    while low <= high:
        mid = (low + high) // 2
        if element == arr[mid]:
            return mid
        elif element < arr[mid]:
            high = mid - 1
        elif element > arr[mid]:
            low = mid + 1
        else:
            return False


result = bs(sort_arr, search_element, n)

if result:
    print("Element {:d} found at position {:d}".format(search_element, result+1))
else:
    print("Element not found.")
