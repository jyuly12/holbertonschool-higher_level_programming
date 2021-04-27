#!/usr/bin/python3
for num in range(0, 8):
    for num1 in range(num + 1, 10):
        print("{:d}{:d},".format(num, num1), end=" ")
num += 1
print("{:d}{:d}".format(num, num1))
