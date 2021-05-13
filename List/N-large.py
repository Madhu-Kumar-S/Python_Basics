# Python program to find N largest elements from a list

lst = eval(input("enter a list:"))

no = int(input("enter how many largest elements to find:"))

def nl(l, n):
    t = l.copy()
    ep = []
    for x in range(n):
        big = 0
        for i in range(len(t)):
            if t[i] > big:
                big = t[i]
        t.remove(big)
        ep.append(big)

    print("{} largest elements are :".format(n))
    for i in ep:
        print(i, end=' ')


nl(lst, no)