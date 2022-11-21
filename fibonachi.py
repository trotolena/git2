def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def count():
    return fib(s + 1)


s = int(input("Enter the steps number (integer): "))
print("Counted ways = ", count())
