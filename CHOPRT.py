T = int(raw_input())
while T:
    a, b = map(int, raw_input().split())
    if a > b:
        print ">"
    elif a < b:
        print "<"
    else:
        print "="
    T -= 1
