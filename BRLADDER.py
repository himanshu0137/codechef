def func(x, y):
    if abs(x-y) > 2:
        return False
    if abs(x-y) == 2:
        return True
    if (x+y+1)%4 == 0:
        return True
    return False  
def main():
    a, b = map(int, raw_input().split())
    if func(a, b):
        return "YES"
    return "NO"
T = int(raw_input())
while T:
    print main()
    T -= 1
