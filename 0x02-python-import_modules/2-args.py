#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = len(argv) - 1
    if number is not 1:
        if number is 0:
            print("{} arguments.".format(number))
        else:
            print("{} arguments:".format(number))
    else:
        print("{} argument:".format(number))

    for count, ch in enumerate(argv):
        if count > 0:
            print("{}: {}".format(count, ch))
