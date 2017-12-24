def pal(s):
    l = len(s)
    if l==1:
        return True
    if l==2:
        if s[0]==s[1]:
            return True
        else:
            return False
    if l%2!=0:
        if s[0:(l-1)/2]==s[((l-1)/2)+1:l][::-1]:
            return True
        else:
            return False
    else:
        if s[0:l/2] == s[l/2:l][::-1]:
            return True
        else:
            return False
def res(s):
    l = len(s)
    for i in range(0,l):
        if s[i]!=s[l-i-1]:
            temp = s[0:i]
            if i+1<l:
                temp+=s[i+1:l]
            if not pal(temp):
                return l-i-1
            else:
                return i
    return -1
n = int(raw_input())
for i in range(0,n):
    s = raw_input()
    print res(s)