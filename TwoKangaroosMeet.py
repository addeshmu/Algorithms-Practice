#!/bin/python

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]


if v1>v2:
    faster = v1
    fastloc = x1
    slower = v2
    slowloc = x2
else:
    faster = v2
    fastloc = x2
    slower = v1
    slowloc = x1

flag =True
dF=fastloc
dS=slowloc
while flag == True:
    if dF == dS:
        print "YES"
        exit(1)
    if dF>dS:
        print "NO"
        exit(1)
    dF += faster
    dS += slower