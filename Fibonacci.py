"""
Fibonacci function to find any Fibonacci series of any length
"""


def fibo(digit):
    if digit == 0:
        return 0

    if digit == 1:
        return 1

    z = fibo(digit - 1) + fibo(digit - 2)
    return z


fibodigit = int(input("How long do you want your Fibonacci series to be: "))

n = 1
while n < fibodigit:

    FibSeries = fibo(n)
    print(FibSeries)
    n += 1

print("FibSeries is done")
