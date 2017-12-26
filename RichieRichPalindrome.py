
def findPal(s,mm, mml,k):
    if mm == k:
        for i in range(0,len(mml)):
            if int(s[mml[i]])>int(s[len(s)-mml[i]-1]):
                s[len(s) - mml[i]-1] = s[mml[i]]
            else:
                s[mml[i]] = s[len(s) - mml[i] - 1]
    else:
        diff = k - mm
        x = len(s)/2+1 if len(s)%2!=0 else len(s)/2
        for i in range(0,x):
            mismatch = 'false' if (s[i] == s[len(s)-i-1]) else 'true'

            if mismatch=='true' and diff>=1:
                if not(int(s[i])==9 or int(s[len(s)-i-1])==9):
                    diff -= 1
                s[len(s) - i - 1] = s[i] = 9

            elif mismatch=='false' and diff>=2 and not(int(s[i])==9):
                s[len(s) - i - 1] = s[i] = 9
                diff -= 2
            elif mismatch == 'false' and diff >= 1 and not(int(s[i])==9):
                if i == len(s) - i - 1:
                    s[i] = 9
                    diff -=1
            elif mismatch=='true':
                if int(s[i]) > int(s[len(s) - i - 1]):
                    s[len(s) - i - 1] = s[i]
                else:
                    s[i] = s[len(s) - i - 1]

    return s

def findMisMatches(n,s):
    mm = 0
    mml = []
    for i in range(0,n/2):
        if s[i]!=s[n-i-1]:
            mm+=1
            mml.append(i)
    return mm,mml

n,k = map(int,raw_input().split())
s = list(raw_input())
mm,mml=findMisMatches(n,s)

if mm>k:
    print -1
else:
    s = findPal(s, mm, mml,k)
    s = ''.join(map(str,s))
    print s
