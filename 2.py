print("w","x","y","z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                f =  (x == (w or y)) or ((w <= z) and (y <= w))
                if f == 0:
                    print(w,x,y,z)


