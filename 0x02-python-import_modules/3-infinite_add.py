#!/usr/bin/python3

import sys

argc = len(sys.argv)
addition = 0

for i in range(1, argc):
    addition += int(sys.argv[i])
print(addition)
