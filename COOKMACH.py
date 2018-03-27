def power2(a):
    n = 0
    while a > 1:
        if a&1:
            return -1
        n += 1
        a = a>>1
    return n
def func(a, b):
    if a == b:
        return 0
    if power2(a) >= 0:
        return abs(power2(a)-power2(b))
    else:
        return 1+func(a>>1, b)
def main():
    a, b = map(int, raw_input().split())
    return func(a, b)
T = int(raw_input())
while T:
    print main()
    T -= 1
