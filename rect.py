import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(raw_input())  # the number of cells on the X axis
height = int(raw_input())  # the number of cells on the Y axis
list=[0 for x in range(0,height)]
for i in xrange(height):
    line = raw_input()  # width characters, each either 0 or .
    list[i]=[ch for ch in  line]
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

for i in range(0,height):
    for j in range(0,width):
        if list[i][j]=='0':
            print j,i,
            if j+1<width and list[i][j+1]=='0' :
                print j+1,i,
            else:
                print -1,-1,
            if i+1<height and list[i+1][j]=='0' :
                print j,i+1
            else:
                print -1,-1