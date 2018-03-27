t = int(raw_input())
while t:
    c, d, l = map(int,raw_input().split())
    if l <= (4*c+4*d) and l%4 == 0:
        if c <= 2*d:
            if l >= 4*d:
                print "yes"
            else:
                print "no"
        else:
            if l >= (4*d + 4*(c-2*d)):
                print "yes"
            else:
                print "no"
    else:
        print "no"
    t -= 1
