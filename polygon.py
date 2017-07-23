def findPoly(n, a):
    if n == 1:
        print 3
        return
    mean = sum(a) / 2

    if n==2:
        if a[0]==a[1]:
            print 1
            return
    count = 0

    for i in range(0, len(a)):
        if a[i] >= mean:
            count += 1

    if count == 0:
        print 0
    else:
        print count


n = int(raw_input().strip())
a = [int(x) for x in raw_input().split()]
findPoly(n,a)