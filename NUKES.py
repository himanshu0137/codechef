a, n, k = map(int, raw_input().split())
i = 0
while i < k:
    print a%(n+1),
    a = a//(n+1)
    i += 1
