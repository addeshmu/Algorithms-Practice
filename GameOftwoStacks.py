#!/bin/python

import sys


def findRec(s, count, a, b):
    if s == x:
        return count
    elif s > x:
        return count - 1
    else:
        return max(findRec(s + a[0], count + 1, a[1:len(a)], b), findRec(s + b[0], count + 1, a, b[1:len(b)]))


def rando(a, b, x1):
    list = [[0 for x in range(0, len(a))] for x in range(0, len(b))]
    for i in range(0, len(b)):
        for j in range(0, len(a)):
            list[i][j] = len(b) - (i)-1 + len(a) - (j)-1

    mx = 0
    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            if list[i][j] > mx:
                if sum(a[0:len(a)-1-j]) + sum(b[0:len(b)-1-i]) <= x1:
                    mx = list[i][j]
                    id = j,i

    print j,i
    return mx


g = int(raw_input().strip())
for a0 in xrange(g):
    n, m, x = raw_input().strip().split(' ')
    n, m, x = [int(n), int(m), int(x)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    print rando(a, b, x)
    # print findRec(0,0,a,b)
    # your code goes here
