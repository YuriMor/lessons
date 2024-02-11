def f(x, result):
    if x > result:
        return 0
    elif x == result:
        return 1
    return f(x+1, result) + f(x*3, result)
print(f(3, 36))