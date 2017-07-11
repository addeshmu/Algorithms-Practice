## Find the number of arrangements for 4XN WALL fixed with 4,1 and 1,4 brick size and then apply sieve of eratostehenes to find number of primes till ans.

T = int(raw_input())
list = []
ways = 0
ops = [[1, 4], [4, 1]]

#efficient
def sieveOfEartosthenes(limit):

    if limit == 1 or limit == 0:
        return 0

    a = [True] * (limit+1)                          # Initialize the primality list
    a[0] =a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in range(i*i, limit+1, i):     # Mark factors non-prime
                a[n] = False

    return a.count(True)

##Inefficient due to append ops
def sieveOfEartosthenes1(n):

    notPrime = []
    if n == 0 or n == 1:
        return 0
    for i in range(2,n+1):
        if i not in notPrime:
            for k in range(i*i,n,i):
                notPrime.append(k)
    return n - len(notPrime)


def findPossibleCombination(dp,item):

    if item >= 4:
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1

        for i in range(4, item+1):
            dp[i] = dp[i-1] + dp[i-4]
        return sieveOfEartosthenes(dp[len(dp)-1])

    else:
        return sieveOfEartosthenes(1)

for i in range(0,T):
    list.append(int(raw_input()))

for item in list:
    dp = [0 for i in range(0, item+1)]
    combos = findPossibleCombination(dp,item)
    print combos