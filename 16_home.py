def f(n):
    if n <= 1:
        return 0
    elif n % 2 == 0:
        return n / 2 + f(n - 1) + 2
    else:
        return f(n - 1) + 3 * n * n
print(f(49))
