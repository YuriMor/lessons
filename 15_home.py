def f(x, y, A):
    return ((x > A) or (y > x) or (2 * y + x < 110))
for A in range(1000)[::-1]:
    podhodit = True
    for x in range(100):
        for y in range(100):
            if not(f(x, y, A)):
                podhodit = False
                break
    if podhodit == True:
        print(A)
