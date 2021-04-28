#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv) - 1
    if number is not 1:
        if number is 0:
            print("{} arguments.".format(number))
        else:
            print("{} arguments:".format(number))
    else:
        print("{} argument:".format(number))

    for i in range(1, len(sys.argv)):
        ch = sys.argv[i]
        print("{}: {}".format(i, ch))
