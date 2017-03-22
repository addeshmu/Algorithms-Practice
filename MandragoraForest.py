##Greedy to solve this

def findAns():
    n = int(raw_input())
    l = [ int(x) for x in raw_input().split()]

    if n== 1:
        print l[0]
        return

    l.sort()

    su = sum(l)
    s = 1
    laste = 0

    for i in xrange(0, n):
        s = s + 1
        su -= l[i]
        e = (su) * s
        if e < laste:
            break
        laste = e

    print laste


def main():
    t = int(raw_input())
    for i in range(0, t):
        findAns()


main()