def main():
    a = [0 for _ in xrange(26)]
    b = [0 for _ in xrange(26)]
    n = len(s)
    for i in xrange(n>>1):
        a[ord(s[i])-97] += 1
        b[ord(s[n-1-i])-97] -= 1
    for i in xrange(26):
        if a[i]+b[i] != 0:
            return "NO"
    return "YES"
T = int(raw_input())
while T:
    s = raw_input()
    print main()
    T -= 1
