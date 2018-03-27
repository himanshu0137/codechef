T = int(raw_input())
while T:
    a = int(raw_input())
    if a&3 == 1:
        print "ALICE"
    else:
        print "BOB"
    T -= 1
