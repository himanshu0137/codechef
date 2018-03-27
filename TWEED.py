T = int(raw_input())
while T:
    n, first = raw_input().split()
    a = map(int, raw_input().split())
    n = int(n)
    if n == 1 and a[0]%2 == 0 and first == "Dee":
        print "Dee"
    else:
        print "Dum"
    T -= 1
