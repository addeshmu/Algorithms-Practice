#!/bin/python

import sys

def findBeautiful(s):
    l = len(s)
    if l==2:
        if int(s[1])-int(s[0])==1:
            return s[0]
        else:
            return 0
    elif l==1:
        return 0
    elif int(s[0])==0:
        return 0
    else:
        flag = False
        for i in range(0,l):
            temp = int(s[0:i+1])+1
            t = len(str(temp))
            if t <=l-i-1:
                if int(s[0:i+1])+1 == int(s[i+1:i+1+t]) and (s[i+1])!='0':
                    flag = True
                    k = i+t+1
                    next = int(s[i+1:i+1+t])+1
                    t = len(str(next))
                    while k+t-1<=l:
                        if int(s[k:k+t]) == next and s[k]!='0':
                            next = int(s[k:k+t])+1
                            k = k+t
                            t  = len(str(next))
                        else:
                            flag = False
                            break
                    if flag:
                        return int(s[0:i+1])

    return 0

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    ans=findBeautiful(s)
    if (ans!=0):
        print "YES",ans
    else:
        print "NO"
