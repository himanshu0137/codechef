def time(n, b, m):
    if n == 1:
        return m
    else:
        if n%2 == 0:
            return n*m/2 + b + time(n/2, b, 2*m)
        else:
            return m*(n+1)/2 + b + time((n-1)/2, b, 2*m)

def main():
    n, b, m = map(int, raw_input().split())
    return time(n, b, m)

T = int(raw_input())
while T:
    print main()
    T -= 1
