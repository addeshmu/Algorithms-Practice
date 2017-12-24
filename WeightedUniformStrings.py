import sys

def weight(c):
    return ord(c) - 96
def process(s):
    u = set()
    start = s[0]
    sum = 0
    i = 1
    startWeight = weight(start)
    sum = startWeight
    u.add(sum)
    while (i<len(s)):
        while(i<len(s) and s[i]==start):
            sum += startWeight
            u.add(sum)
            i+=1
        if(i<len(s)):
            start = s[i]
            startWeight = weight(start)
            sum = startWeight
            u.add(sum)
        i += 1
    return u
s = raw_input()
n = int(raw_input())
u = process(s)
for x in range(0,n):
    if int(raw_input()) in u :
        print 'Yes'
    else:
        print 'No'




