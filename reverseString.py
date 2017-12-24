def recurse(a):

    if len(a)==0:
        return
    print a[len(a)-1],
    recurse(a[:len(a)-1])


def efl(a,l):
    if len(a)==0 and len(l.keys())>0:
        print "not found"
        return
    if len(l.keys())==0:
        print "found"
        return
    if a[0] in l.keys():
        del l[a[0]]
    efl(a[1:len(a)],l)



a = raw_input()
l ={}
l['e'] =1
l['l'] =1
l['f'] =1

efl(a,l)
