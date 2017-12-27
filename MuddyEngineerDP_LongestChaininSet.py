# Complete the function below.
def findChain(word, wm, S):
    longest = 1
    l = len(word)
    visited = []
    for i in range(0, l):
        s = word[0:i]
        if i + 1 < l:
            s += word[i + 1:l]
        if s in wm.keys():
            le = wm[s] + 1
            longest = max(longest, le)
    return longest


def longestChain(words):
    if len(words) == 0:
        return 0
    lw = len(words)
    mp = []
    S = set()
    for each in words:
        mp.append((each, len(each)))
        S.add(each)
    import operator
    mp = sorted(mp, key=operator.itemgetter(1))

    wm = {}

    wm[mp[0][0]] = 0
    chainLen = []
    longest = 0
    for i in range(0, lw):
        chainLen.append(0)
    for i in range(0, lw):
        word = mp[i][0]
        chainLen[i] = findChain(word, wm, S)
        longest = max(longest, chainLen[i])
        wm[mp[i][0]] = chainLen[i]

    return longest


words=[]
for i in range(0,10):
    words.append(raw_input())

print longestChain(words)