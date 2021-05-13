# Python program to swap two elements in a list

l = [1, 2, 3, 4, 5]

print("enter the position of any 2 elements to swap:\n")

p1, p2 = [int(x) for x in input().split()]

print("you entered position 1= {} , position 2= {}".format(p1, p2))

print("before swapping")
print(l)
print("after swapping")

l[p1-1], l[p2-1] = l[p2-1], l[p1-1]

print(l)