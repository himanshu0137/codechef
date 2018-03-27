def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    return min(a)*(n-1)

T = int(raw_input())
while T:
    print main()
    T -= 1
