#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_argc = len(sys.argv) - 1
    if num_argc == 0:
        print("0 arguments.")
    elif num_argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_argc))

    for i in range(1, num_argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
