#Longest Common Subsequence
import sys

def commonChild():
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    listx = [ [0] * 5001 ] * 2
    mx = 0
    for i in xrange(1, len(s2) + 1):
        for j in xrange(1, len(s1) + 1):
            if s2[i - 1] == s1[j - 1]:
                listx[1][j] = listx[0][j - 1] + 1
            else:
                listx[1][j] = listx[0][j] if listx[0][j]>listx[1][j - 1] else listx[1][j - 1]
            if mx < listx[1][j]:
                mx = listx[1][j]
        listx[0] = listx[1]
        listx[1] = [0]*(len(s2)+1)

    print mx


commonChild()