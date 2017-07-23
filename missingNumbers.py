
def main():
    n= int(raw_input())
    a = [int(x) for x in raw_input().split()]
    m = int(raw_input())
    b = [int(x) for x in raw_input().split()]

    a.sort()
    b.sort()

    missing = set()
    k=0
    for i in range(0,len(b)):
        if k<len(a):
            if a[k]<>b[i]:
                missing.add(b[i])
            if a[k]==b[i]:
                k+=1
        else:
            missing.add(b[i])

    for s in sorted(missing):
        print s,

main()