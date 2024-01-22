print("w","x","y","z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                f = ((x and w) or (w and z)) == ((z <= y) and (y <= x))
                if f == 1:
                    print(w, x, y, z, f)



