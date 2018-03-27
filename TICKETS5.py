def check(s):
    if s[0] == s[1]:
        return "NO"
    i = 2
    while i < len(s)-1:
        if s[i] != s[0] or s[i+1] != s[1]:
            return "NO"
        i += 2
    return "YES"
def main():
    t = int(raw_input())
    while t:
        s = raw_input()
        print check(s)
        t -= 1

main()