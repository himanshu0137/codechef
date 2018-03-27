def check(n):
    if n%2 == 0:
        for i in xrange(26):
            if alpha[i] == n/2:
                return "YES"
    return "NO"
T = int(raw_input())
while T:
    alpha = [0 for _ in xrange(26)]
    s = raw_input()
    for q in s:
        alpha[ord(q)-97] += 1
    print check(len(s))
    T -= 1
