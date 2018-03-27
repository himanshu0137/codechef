def func(x, y):
    if x == y:
        return True
    i = 0
    j = 0
    while 1:
        if i >= len(x):
            return False
        if j >= len(y):
            return True
        if x[i] == y[j]:
            j += 1
        i += 1
def main():
    m, w = raw_input().split()
    a = False
    if len(m) >= len(w):
        a = func(m, w)
    else:
        a = func(w, m)
    if a:
        return "YES"
    return"NO"
T = int(raw_input())
while T:
    print main()
    T -= 1
