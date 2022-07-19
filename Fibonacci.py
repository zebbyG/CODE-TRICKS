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


while True:
    try:
        fibolen = int(input("How long do you want your Fibonacci series to be: "))
        break
    except ValueError:
        print("Please enter a number")

for n in range(fibolen):
    print(fibo(n))

print("Fibonacci series done")
