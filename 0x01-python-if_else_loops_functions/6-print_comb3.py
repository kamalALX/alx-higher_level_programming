#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (i != j and i < j):
            print(str(i) + str(j), end="")
            if (str(i) + str(j) != "89"):
                print(" ,", end ="")
            else:
                print("")
