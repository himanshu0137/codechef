T = int(raw_input())
while T:
    s = raw_input()
    f = 0
    for i in xrange(len(s)-2):
        if s[i:i+3] == "101" or s[i:i+3] == "010":
            f = 1
            break
    if f:
        print "Good"
    else:
        print "Bad"
    T -= 1
