def func(a ,n):
    if n == 1 and a[0] == "cookie":
        return "NO"
    for i in xrange(n-1):
        if a[i] == "cookie" and a[i+1] != "milk":
            return "NO"
        return "YES"
def main():
    n = int(raw_input())
    a = raw_input().split()
    return func(a, n)
T = int(raw_input())
while T:
    print main()
    T -= 1
