T = int(raw_input())
while T:
    n, m = map(int, raw_input().split())
    if n*m%2 == 0:
        print "Yes"
    else:
        print "No"
    T -= 1
