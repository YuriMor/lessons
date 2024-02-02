n = 9 ** 11 * 3 ** 20 - 3 ** 8 - 27
k = 0
while n > 0:
    if n % 3 == 2:
        k += 1
    n = n // 3
print(k)



