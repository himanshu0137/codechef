p = int(raw_input())
while p:
    s, sg, fg, d, t = map(float, raw_input().split())
    v = 180*d/t + s
    sd = abs(v-sg)
    fd = abs(v-fg)
    if sd > fd:
        print "FATHER"
    elif sd < fd:
        print "SEBI"
    else:
        print "DRAW"
    p -= 1
