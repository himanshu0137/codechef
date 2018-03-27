t = int(raw_input())
while t:
    s = raw_input()
    stud = 0
    for i in xrange(len(s)-1):
        if s[i] == '<' and s[i+1] == '>':
            stud += 1
    print stud
    t -= 1
    