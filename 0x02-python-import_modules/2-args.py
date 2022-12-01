#!/usr/bin/python3
import sys
l = len(sys.argv)
if l == 0:
    print("{} arguments.".format(l))
else:
    print("{} arguments:".format(l))
    for i in range(l):
        print("{}: {}".format(i, sys.argv[i + 1])
