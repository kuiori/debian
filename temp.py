#! /usr/bin/env python3
import sys
sys.setrecursionlimit(100000)


def digui(n):
    if n == 1:
        return 1
    else:
        return n * digui(n - 1)
result = digui(100)
print(result)
time = 0
while True:
    if result % 10 == 0:
        result //= 10
        time += 1
    else:
        break
print(time)
