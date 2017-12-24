
def recurse(str,i,j):
    if i==j:
        print ''.join(e for e in str)
        return

    for k in range(i,j):
        temp = str[k]
        str[k] = str[i]
        str[i] = temp
        recurse(str,i+1,j)
        temp = str[k]
        str[k] = str[i]
        str[i] = temp


str = raw_input()


recurse([x for x in str],0,len(str))