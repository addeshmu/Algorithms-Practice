def spamClusterization(requests, IDs,threshold):
    list1 = []
    for each in requests:
        '''ans = each.replace('!', " ").replace(",", " ").replace(".", " ").replace("?", " ").lower()
        # ans = ''.join(e for e in each.lower() if e.isalnum() or e==" ")
        ans = ans.split(" ")
        i = 0
        while i<len(ans):
            if ans[i] == '' or ans[i]==" ":
                del ans[i]
            else:
                i+=1'''
        ans = []
        str = ''
        for e in each:
            if e.isalnum():
                str += e
            else:
                if str!='':
                    ans.append(str.lower())
                str=''
                # ans = ans.split(" ")
            if each.index(e)==len(each)-1:
                if str != '':
                    ans.append(str.lower())
        list1.append(set(sorted(ans)))
    res = {}
    i = j = 0
    while i < len(list1):
        j = 0
        while j < len(list1):
            if i != j:
                jacc = float(len(list1[i].intersection(list1[j]))) / float(len(list1[i].union(list1[j])))
                if jacc >= threshold:
                    flag = False
                    if i in res.keys():
                        res[i].add(IDs[j])
                    else:
                        res[i] = set([IDs[j]])
                    if j in res.keys():
                        res[i] = res[i].union(res[j])
                        res.pop(j, None)
            j += 1
        i += 1
    finallist = []
    for x in res.keys():
        finallist.append(sorted(list(res[x])))
    print sorted(finallist)



requests = ["I need a new window.",
            "I really, really want to replace my window!",
            "Replace my window.",
            "I want a new window.",
            "I want a new carpet, I want a new carpet, I want a new carpet.",
            "Replace my carpet"]

requests1 = ["I need a new window",
 "I really, really want to replace my window",
 "Replace mY !!.windoW........",
 "I want a new window?",
 "I want a new carpet, i want a new carpet, I WANT A NEW CARPET",
 "RePlAcE!!! !!!My!!! !!!CaRpEt!!!!"]

requests1= ["Wow So Cute!! wow wow",
 "So cute, wow! Cute cute cute"]

requests1= ["A",
 "C",
 "A C"]
spamClusterization(requests,[374, 2845, 83, 1848, 1837, 1500],0.5)