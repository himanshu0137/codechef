t = int(raw_input())
while t:
    n = int(raw_input())
    a = raw_input().split()
    count = 0
    for i in a:
        if i == "1":
            count += 1
    if count%2 == 0:
        print n-count
    else:
        print count
    t -= 1
    