#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add_num = 0
    for i in range(1, len(sys.argv)):
        add_num += int(sys.argv[i])
    print("{}".format(add_num))
