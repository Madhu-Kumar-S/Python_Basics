# Break a list into chunks of size N in Python
ml = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("original list is",ml)
nl = []

break_point = 3

if break_point > len(ml):
    print("cant be break a list into chunks as break point is",break_point)
else:
    for i in range(break_point + 1):
        nl.append(ml[:break_point])
        for j in ml[:break_point]:
            ml.remove(j)
    print("chunked list is ",nl)