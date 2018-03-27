T = int(raw_input())
while T:
    N = int(raw_input())
    s = ""
    if 360%N == 0:
        s += "y "
    else:
        s += "n "
    if N <= 360:
        s += "y "
    else:
        s += "n "
    if N <= 26:
        s += "y"
    else:
        s += "n"
    print s
    T -= 1
