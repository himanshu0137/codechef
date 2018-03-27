def func(n,s):
    for i in xrange(n-1):
        if s[i] > s[i+1]:
            return True
    return False
def main():
    n = int(raw_input())
    s = map(int,raw_input().split())
    if func(n,s) and n*(n+1)/2 == sum(s):
        return "yes"
    return "no"
T = int(raw_input())
while T:
    print main()
    T -= 1
