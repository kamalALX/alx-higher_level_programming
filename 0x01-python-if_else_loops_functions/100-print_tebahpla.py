#!/usr/bin/python3

i = 0
for character in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(character - i)), end="")
    i = 32 if i == 0 else 0
