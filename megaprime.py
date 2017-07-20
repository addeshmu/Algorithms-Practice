n = raw_input()
s = 0
i = 0
flag = False
if n[0] == '-':
    flag = True
    n = n[1:len(n)]

for i in range(0, len(n)):
    s += int(n[i])

while (len(str(s)) > 1):
    t = 0
    for i in str(s):
        t += int(i)
    s = t

if flag:
    print '-' + str(s)
else:
    print s