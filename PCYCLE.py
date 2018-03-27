n = int(raw_input())
a = map(int, raw_input().split())
b = []
c = 0
visited = [False for _ in xrange(n)]
for i in xrange(n):
    j = 0
    if not visited[i]:
        b.append([i+1])
        j += i
        while i+1 != a[j]:
            b[c].append(a[j])
            visited[j] = True
            j = a[j]-1
        visited[j] = True
        b[c].append(i+1)
        c += 1
print c
for i in b:
    print " ".join(map(str, i))
