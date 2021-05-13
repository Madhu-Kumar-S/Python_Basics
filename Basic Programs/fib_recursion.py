# Python Program for n-th Fibonacci number using Recursion & memoization
from functools import lru_cache #least recently used cache

@lru_cache(maxsize=1000)
def fibonacci(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

no = int(input("enter upto how many terms:"))

for i in range(1, no + 1):
    print(i, ":", fibonacci(i))

