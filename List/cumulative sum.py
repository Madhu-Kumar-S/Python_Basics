#Python program to find Cumulative sum of a list

l = [10, 20, 30, 40, 50]


for i in range(len(l)-1):
    l[i+1] = l[i+1] + l[i]

print("cumulative sum of a list1 is :",l)


list = [10, 20, 30, 40, 50]
new_list = []
j = 0
for i in range(0, len(list)):
    j += list[i]
    new_list.append(j)

print("cumulative sum of a list2 is :",new_list)