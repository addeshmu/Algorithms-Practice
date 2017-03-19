import math


def sideFinder(x, y, x1, y1, x2, y2):
    lineP1P2 = ((float(x - x2) * float(y1 - y2)) - (float(y - y2) * float(x1 - x2)))

    # lineP1P2 = float(y - y1 - m*(x-x1))

    if lineP1P2 > 0:
        return '+'
    elif lineP1P2 < 0:
        return '-'
    else:
        return 'on'


w, h = raw_input().strip().split(' ')
w, h = [float(w), float(h)]
circleX, circleY, r = raw_input().strip().split(' ')
circleX, circleY, r = [int(circleX), int(circleY), int(r)]
x1, y1, x3, y3 = raw_input().strip().split(' ')
x1, y1, x3, y3 = [int(x1), int(y1), int(x3), int(y3)]

l = [['.' for x in range(0, int(w))] for m in range(0, int(h))]
'''
for i in range(0, int(h)):
    for j in range(0, int(w)):
        d = math.pow((circleX - j), 2) + math.pow((circleY - i), 2)
        if d <= r * r:
            l[i][j] = '#'
'''
x4 = (float(x1 + x3 + y1 - y3) / float(2))
y4 = (float(y1 + y3 + x1 - x3) / float(2))
x2 = (float(x1 + x3 + y3 - y1) / float(2))
y2 = (float(y1 + y3 + x3 - x1) / float(2))



xc = (x1+x3)/2
yc = (y1+y3)/2
xd = (x1-x3)/2
yd = (y1-y3)/2
print xc-yd,xc+yd,yc+xd,yc-xd
print x4,y4,x2,y2
x4 = xc-yd
x2 = xc+yd
y4 = yc+xd
y2 = yc-xd
midx = (x1 + x3) / 2
midy = (y1 + y3) / 2

linep1p2 = sideFinder(midx, midy, x1, y1, x2, y2)
linep2p3 = sideFinder(midx, midy, x2, y2, x3, y3)
linep3p4 = sideFinder(midx, midy, x3, y3, x4, y4)
linep4p1 = sideFinder(midx, midy, x4, y4, x1, y1)

for i in range(0, int(h)):
    for j in range(0, int(w)):
        # if sideFinder(j,i,x1,y1,x2,y2)== linep1p2 and sideFinder(j,i,x2,y2,x3,y3)==linep2p3 and sideFinder(j,i,x3,y3,x4,y4)==linep3p4 and sideFinder(j,i,x4,y4,x1,y1)==linep4p1:
        if sideFinder(j, i, x1, y1, x2, y2) != sideFinder(j, i, x4, y4, x3, y3) and sideFinder(j, i, x2, y2, x3,
                                                                                               y3) != sideFinder(j, i,
                                                                                                                 x1, y1,
                                                                                                                 x4,
                                                                                                                 y4):
            l[i][j] = "#"
        elif (sideFinder(j, i, x1, y1, x2, y2) == 'on' and (x1 <= j <= x2 or x2 <= j <= x1) and (
                    y1 <= i <= y2 or y2 <= i <= y1)) or (
                    sideFinder(j, i, x2, y2, x3, y3) == 'on' and (x2 <= j <= x3 or x3 <= j <= x2) and (
                    y3 <= i <= y2 or y2 <= i <= y3)) or (
                    sideFinder(j, i, x3, y3, x4, y4) == 'on' and (x3 <= j <= x4 or x4 <= j <= x3) and (
                    y4 <= i <= y3 or y3 <= i <= y4)) or (
                    sideFinder(j, i, x4, y4, x1, y1) == 'on' and (x4 <= j <= x1 or x1 <= j <= x4) and (
                    y4 <= i <= y1 or y1 <= i <= y4)):
            l[i][j] = "#"

str1 = ''
for i in l:
    for j in range(0, len(i)):
        str1 += i[j]
    str1 += '\n'
print str1

