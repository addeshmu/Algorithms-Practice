#!/bin/python

import sys


g = int(raw_input().strip())
for a0 in xrange(g):
    n = int(raw_input().strip())
    p = map(int,raw_input().strip().split(' '))
        # your code goes here
    if p[0]%2==0:
        temp = p[0]-1
    else:
        temp = p[0]+1
    for j in range(1,len(p)):
        if p[j]%2==0:
            temp = temp ^ (p[j]-1)
        else:    
            temp = temp^(p[j]+1)
    if temp==0:
        print "L"
    else:
        print "W"
