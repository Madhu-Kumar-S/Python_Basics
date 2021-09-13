# Bubble sort in array
import array

elements = [int(x) for x in input("enter the elements:").split()]
arr = array.array('i', elements)
print("array is:", *elements)


def sort(x):
    flag = False
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if x[j] > x[j+1]:
                temp = x[j]  # can use x[j], x[j + 1] = x[j + 1], x[j]
                x[j] = x[j+1]
                x[j+1] = temp
                flag = True
        if flag == False:
            break
        else:
            flag = False
    print("Sorted array is:", *x)


sort(arr)
