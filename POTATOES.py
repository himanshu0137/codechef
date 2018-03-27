def isprime(a):
    if a == 3:
        return True
    for i in xrange(2, a/2):
        if a%i == 0:
            return False
    return True
def main():
    x, y = map(int, raw_input().split())
    if (x+y)%2 == 0:
        z = 1
    else:
        z = 2
    while 1:
        if isprime(x+y+z):
            return z
        z += 2
T = int(raw_input())
while T:
    print main()
    T -= 1
