t = int(raw_input())
def func(a,b):
    A = True if a=="W" else False
    B = True if b=="W" else False
    if((not A) & (not B)):
        return "W"
    else:
        return "B"
while(t):
    x = raw_input()
    y = raw_input()
    s = ""
    for i in xrange(len(x)):
        s += func(x[i],y[i])
    print(s)
    t -= 1