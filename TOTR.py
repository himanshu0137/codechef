t, m = raw_input().split()
t = int(t)
while t:
    a = list(raw_input())
    i = 0
    while i < len(a):
        if a[i] in ["_", ",", ".", "?", "!"]:
            i += 1
            continue
        if ord(a[i]) < 97:
            a[i] = chr(ord(m[ord(a[i])-65])-32)
        else:
            a[i] = m[ord(a[i])-97]
        i += 1
    print "".join(a)
    t -= 1
