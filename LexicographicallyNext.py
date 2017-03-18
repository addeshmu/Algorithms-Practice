def findLexicoNext(s):

    n = len(s)

    if n == 1:
        print "no answer"
        return

    i = n-1

    while i>0 and s[i-1]>=s[i]:
        i -= 1

    if i <=0:
        print "no answer"
        return

    j = n - 1

    while j > 0 and s[j]<=s[i-1]:
        j -= 1

    s[i-1],s[j] = s[j],s[i-1]
    s[i:] = s[n-1:i-1:-1]
    print ''.join(s)



def main():
    T = int(raw_input())
    for i in range(0,T):
        s = [x for x in raw_input()]
        findLexicoNext(s)

main()