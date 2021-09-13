# Bubble sort using array array
import array

print("................Bubble Sort...............")
elements = [int(x) for x in input("enter the elements:").split()]
arr = array.array('i', elements)
print("array is:", *elements)


def bs_sort(x):
    n = len(arr)
    flag = False
    for i in range(n-1):
        for j in range(n-1-i):
            if x[j] > x[j+1]:
                temp = x[j]  # can use x[j], x[j + 1] = x[j + 1], x[j]
                x[j] = x[j+1]
                x[j+1] = temp
                flag = True
        if not flag:
            break
        else:
            flag = False
    return x


x = bs_sort(arr)
print("Sorted array is:", *x)

"""
Sample
enter the elements: 44 16 83 7 67 21
array is: 44 16 83 7 67 21
array('i', [16, 44, 83, 7, 67, 21])
array('i', [16, 44, 83, 7, 67, 21])
array('i', [16, 44, 7, 83, 67, 21])
array('i', [16, 44, 7, 67, 83, 21])
array('i', [16, 44, 7, 67, 21, 83])
end inner loop 0
array('i', [16, 44, 7, 67, 21, 83])
array('i', [16, 7, 44, 67, 21, 83])
array('i', [16, 7, 44, 67, 21, 83])
array('i', [16, 7, 44, 21, 67, 83])
end inner loop 1
array('i', [7, 16, 44, 21, 67, 83])
array('i', [7, 16, 44, 21, 67, 83])
array('i', [7, 16, 21, 44, 67, 83])
end inner loop 2
array('i', [7, 16, 21, 44, 67, 83])
array('i', [7, 16, 21, 44, 67, 83])
end inner loop 3
break
Sorted array is: 7 16 21 44 67 83
"""
