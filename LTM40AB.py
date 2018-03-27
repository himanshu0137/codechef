t = int(raw_input())
while t:
    a, b, c, d = map(int, raw_input().split())
    sol = 0
    if a < b and c < d and a < d:
        if c <= b:
            sol = (b-a+1)*(max(b, d)-b) + (max(c, a)-a)*(min(b, d)-c+1) + ((min(b, d)-max(c, a)+1)*(min(b, d)-max(a, c)))/2
        else:
            sol = (b-a+1)*(d-c+1)
    print sol
    t -= 1
