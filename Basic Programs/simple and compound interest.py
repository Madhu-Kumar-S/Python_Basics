# Python Program for simple interest and compound interest

def si(p, r, t):

    res1 = p * r/100 * t
    return res1

def ci(p, r, t):

    res2 = (p * ((1 + (r/100))**t)) - p
    return res2


principle = int(input("enter the principle amount:"))

rate = int(input("enter the rate of percentage:"))

time = int(input("enter the time in years:"))

result1 = si(principle, rate, time)

result2 = ci(principle, rate, time)

print("simple interest is {:.2f}".format(result1))

print("compound interest is {:.2f}".format(result2))

