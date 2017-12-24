#!/bin/python

import sys
s  = raw_input()

def process(s):
    n  = len(s)
    i =0
    while (i<n):
        if (i<n-1):
            if s[i]==s[i+1]:
                temp = s
                s = temp[0:i]
                if(i+2<n):
                    s += temp[i+2:n]
                    if i!=0:
                        i=i-1
                n = len(s)
            else:
                i+=1
        else:
            i +=1
    return s

new = process(s)

if new!='':
    print new
else:
    print 'Empty String'